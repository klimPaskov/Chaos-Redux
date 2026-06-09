# Event005 Soviet Collapse Focus Tree Full Read-Only Audit

Date: 2026-06-04 16:32 UTC
Role: `chaosx_focus_tree_auditor`
Scope: full Soviet Collapse focus-tree audit for the active Event005 rework.

No gameplay, localisation, asset, or flag sprite files were edited. This report is the only file written.

## References Consulted

Project guidance:

- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Offline Paradox wiki snapshot:

- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`

Vanilla docs/examples:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Vanilla focus files sampled: `common/national_focus/soviet.txt`, `poland.txt`, `uk.txt`

Event005 specs/plans inspected:

- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `docs/plans/005_soviet_collapse_plans/2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md`

## Count Summary

Corrected parser totals:

- Focus trees audited: 41
- Focus blocks audited: 1,698
- Duplicate focus IDs: 0
- Direct `add_ideas` / `remove_ideas` / `swap_ideas` / `add_timed_idea` / `modify_ideas` calls inside focus completion rewards: 0
- Duplicate absolute focus coordinates after top-level-only coordinate parsing: 0
- Tight adjacent focus pairs, <= 1 x/y unit: 883
- Prerequisite geometry risks: 223
- Same-row mutual-exclusion pathline risks: 114
- Focuses calling generic `soviet_collapse_apply_focus_*` helpers: 1,022
- Focuses with equipment rewards: 170
- Focuses with PP/stability/war support rewards: 416
- Focuses with building rewards: 415
- Focuses with claim/war rewards: 29
- Focuses with decision unlocks/tooltips: 100
- Focuses with unit/manpower/template-like rewards: 108

By file:

| File | Trees | Focuses |
| --- | ---: | ---: |
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1,005 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |

By tree/tag:

| File | Tree | Tags | Focuses |
| --- | --- | --- | ---: |
| republics | `soviet_collapse_ukraine_focus_tree` | UKR | 83 |
| republics | `soviet_collapse_breakaway_focus_tree` | generic event-created republics | 36 |
| republics | `soviet_collapse_internal_republic_focus_tree` | KAR, KOM, CRI, TAT, BSK, FER, YAK, BYA, TAN | 62 |
| republics | `soviet_collapse_baltic_focus_tree` | LIT, LAT, EST | 42 |
| republics | `soviet_collapse_caucasus_focus_tree` | GEO, ARM, AZR | 40 |
| republics | `soviet_collapse_central_asia_focus_tree` | UZB, KYR, TAJ, TMS | 45 |
| republics | `soviet_collapse_moldova_focus_tree` | MOL | 48 |
| republics | `soviet_collapse_belarus_focus_tree` | BLR | 53 |
| republics | `soviet_collapse_kazakhstan_focus_tree` | KAZ | 92 |
| custom splinters | `FTH_soviet_collapse_focus_tree` | FTH | 47 |
| custom splinters | `PRA_soviet_collapse_focus_tree` | PRA | 22 |
| custom splinters | `TSC_soviet_collapse_focus_tree` | TSC | 18 |
| custom splinters | `RMC_soviet_collapse_focus_tree` | RMC | 18 |
| custom splinters | `DSC_soviet_collapse_focus_tree` | DSC | 18 |
| custom splinters | `NRF_soviet_collapse_focus_tree` | NRF | 18 |
| custom splinters | `ICD_soviet_collapse_focus_tree` | ICD | 18 |
| custom splinters | `BSC_soviet_collapse_focus_tree` | BSC | 47 |
| custom splinters | `TNC_soviet_collapse_focus_tree` | TNC | 47 |
| custom splinters | `ALA_soviet_collapse_focus_tree` | ALA | 47 |
| custom splinters | `BBH_soviet_collapse_focus_tree` | BBH | 47 |
| custom splinters | `KRS_soviet_collapse_focus_tree` | KRS | 47 |
| custom splinters | `UDC_soviet_collapse_focus_tree` | UDC | 47 |
| custom splinters | `SDZ_soviet_collapse_focus_tree` | SDZ | 47 |
| custom splinters | `GAC_soviet_collapse_focus_tree` | GAC | 47 |
| custom splinters | `DHC_soviet_collapse_focus_tree` | DHC | 47 |
| custom splinters | `KHC_soviet_collapse_focus_tree` | KHC | 47 |
| custom splinters | `FEV_soviet_collapse_focus_tree` | FEV | 47 |
| custom splinters | `SZA_soviet_collapse_focus_tree` | SZA | 47 |
| custom splinters | `UWD_soviet_collapse_focus_tree` | UWD | 47 |
| custom splinters | `MRC_soviet_collapse_focus_tree` | MRC | 47 |
| custom splinters | `IUL_soviet_collapse_focus_tree` | IUL | 47 |
| custom splinters | `BAC_soviet_collapse_focus_tree` | BAC | 47 |
| custom splinters | `ARD_soviet_collapse_focus_tree` | ARD | 47 |
| custom splinters | `NLC_soviet_collapse_focus_tree` | NLC | 47 |
| factory successors | `CFR_soviet_collapse_focus_tree` | CFR | 47 |
| factory successors | `OGB_soviet_collapse_focus_tree` | OGB | 23 |
| factory successors | `MFR_soviet_collapse_focus_tree` | MFR | 58 |
| ancient restorations | `KZR_soviet_collapse_ancient_focus_tree` | KZR | 16 |
| ancient restorations | `SOG_soviet_collapse_ancient_focus_tree` | SOG | 16 |
| ancient restorations | `KHW_soviet_collapse_ancient_focus_tree` | KHW | 16 |
| ancient restorations | `ALN_soviet_collapse_ancient_focus_tree` | ALN | 16 |

## Idea Reward and Idea Lifecycle Findings

The four focus files do not directly add, remove, swap, or modify ideas in focus completion rewards. That means there were no direct same-focus duplicate idea adds and no direct long `add_ideas = { ... }` stacks in focus files.

The reported idea spam is still supported by evidence, but it is indirect through scripted effect chains:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5561` - `soviet_collapse_clear_republic_staged_ideas` removes a very long list of staged republic ideas. The parser counted 96 direct idea tokens in that block because each idea appears in `has_idea` and `remove_ideas`.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5731` - `soviet_collapse_clear_focus_starting_tension_ideas` clears startup/rivalry spirits for PRA, TSC, RMC, DSC, NRF, ICD, and OGB.
- `common/scripted_effects/005_soviet_collapse_effects.txt:7797` - `soviet_collapse_update_pra_authority_idea` repeatedly clears and replaces PRA authority ideas based on focus flags.
- `common/scripted_effects/005_soviet_collapse_effects.txt:4745` and `:4792` - republic recovery helpers swap/remove startup disorder ideas.
- `common/scripted_effects/005_soviet_collapse_effects.txt:17509`, `:17945`, `:17758` - successor setup helpers add identity ideas for DSC, NRF, OGB, and the other high-chaos states.
- `common/scripted_effects/005_soviet_collapse_effects.txt:11960` - MFR helper adds `mfr_arsenal_quotas`.

The biggest design risk is not literal duplicated focus rewards anymore; it is that 1,022 focuses call generic `soviet_collapse_apply_focus_*` helpers, many of which route into staged progress, recovery, idea cleanup, high-chaos payload, and generic reward packets. The most repeated helpers are:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 138 focus calls
- `soviet_collapse_apply_focus_military_consolidation`: 131
- `soviet_collapse_apply_focus_legal_recognition`: 107
- `soviet_collapse_apply_focus_republican_compact_plan`: 96
- `soviet_collapse_apply_focus_foreign_channel`: 65
- `soviet_collapse_apply_focus_security_supply_plan`: 64
- `soviet_collapse_apply_focus_high_chaos_identity`: 57
- `soviet_collapse_apply_focus_league_preparation`: 51
- `soviet_collapse_apply_focus_chaos_assault_plan`: 47
- `soviet_collapse_apply_focus_foreign_recognition_plan`: 42

Priority fix: do not add more one-focus-one-spirit rewards. Instead, parent should centralize idea lifecycles into visible starting spirits plus hidden upgrade/replace helpers, and make focus tooltips communicate route changes rather than expose cleanup.

## Generic and Shallow Reward Patterns

The reward pattern has improved from earlier idea-stack reports, but the current trees still lean heavily on reusable generic helpers and flat bundles. This is especially visible in custom splinters where many 47-focus trees share a skeleton: `first_guard`, `stores`, `legitimacy`, `rival`, `economy`, `league`, `settlement`, `industry_plan`, `diplomatic_plan`, `war_plan`, `future/endgame`. The skeleton gives breadth, but many tags still feel like a renamed version of the same helper calls.

Examples:

- `FTH_birth`, `FTH_first_guard`, `FTH_stores`, `FTH_legitimacy`, `FTH_rival`, `FTH_doctrine`, `FTH_economy`, `FTH_league` show the common custom-splinter pattern: variables, PP/stability, then generic chaos assault/supply/legal/league helpers.
- `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` largely use the same 47-focus depth, so parent should vary mechanics and end-state branch logic by identity rather than only localise names and swap one or two payloads.
- Ancient restoration trees are compact and heavily helper/variable driven. They have some claims and decision tooltips, but each 16-focus tree needs one more distinctive mechanic loop to avoid reading as "claims plus old-name legitimacy".
- Railway/factory states have stronger identity hooks than generic splinters, but still repeat construction, rail, offsite factory, equipment, and PP/stability rewards. CFR and MFR are the most mechanically promising but need the reward payloads consolidated into construction/arsenal decision systems.

## Layout and Pathline Risks

Corrected layout parser note: an earlier loose parser can falsely report duplicate coordinates by reading nested `x`/`y` values. The corrected top-level-only parser found no duplicate absolute focus coordinates in the four files.

However, layout risk remains high:

- 883 very tight adjacent focus pairs.
- 223 prerequisite geometry risks where prerequisites are not visually above children or have wide short drops likely to create awkward lines.
- 114 same-row mutual-exclusion risks where the red pathline may pass through unrelated focuses.
- Layout cannot be visually verified from script alone. These findings are coordinate/pathline heuristics and should be checked in-game or via focus rendering by the parent.

Highest-risk trees by corrected parser:

- `CFR_soviet_collapse_focus_tree`: 32 tight pairs, 12 prerequisite geometry risks, 24 same-row mutual-exclusion risks.
- `soviet_collapse_kazakhstan_focus_tree`: 72 tight pairs, 24 prerequisite geometry risks, 4 same-row mutual-exclusion risks.
- `soviet_collapse_ukraine_focus_tree`: 51 tight pairs, 14 prerequisite geometry risks, 4 same-row mutual-exclusion risks.
- `soviet_collapse_moldova_focus_tree`: 26 tight pairs, 12 prerequisite geometry risks, 6 same-row mutual-exclusion risks.
- `soviet_collapse_central_asia_focus_tree`: 25 tight pairs, 12 prerequisite geometry risks, 6 same-row mutual-exclusion risks.
- `soviet_collapse_internal_republic_focus_tree`: 59 tight pairs, 8 prerequisite geometry risks, 6 same-row mutual-exclusion risks.
- `MFR_soviet_collapse_focus_tree`: 39 tight pairs, 12 prerequisite geometry risks.
- `soviet_collapse_belarus_focus_tree`: 23 tight pairs, 8 prerequisite geometry risks, 4 same-row mutual-exclusion risks.

Specific pathline risks:

- `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`: all are same-row mutually exclusive governance choices around y=6. Red exclusion lines can cross sibling focuses.
- `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`: same-row strategy fork around y=9 has the same issue.
- `internal_soviet_collapse_security_council` vs `internal_soviet_collapse_border_and_rail_liaisons`: same-row mutual exclusion has `internal_soviet_collapse_legal_autonomy_congress` between them.
- `moldova_soviet_collapse_conditional_union` vs `moldova_soviet_collapse_reject_the_union_question`: same-row mutual exclusion has `moldova_soviet_collapse_alliance_not_union` between them.
- Ukraine early/foreign branch tightness around `ukr_soviet_collapse_war_without_a_declaration`, `ukr_soviet_collapse_open_the_liaison_offices`, and `ukr_soviet_collapse_black_sea_port_ledgers`.
- Belarus rail/corridor pathing has wide short drops from `blr_soviet_collapse_the_rail_map_on_the_wall` to later nodes.
- Kazakhstan has the broadest coordinate spread and many wide short drops around `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_resource_defense_directorate`, and southern/steppe federation nodes.

Continuous focus panel risk: all audited trees place continuous focus panels to the right with large pixel x values. No script-only overlap candidate was found, but this still needs visual verification because the visible tree width varies by route.

## Route-Depth Gaps by Group

### Ukraine

Ukraine is the strongest republic tree in count and branch variety, but some route branches still feel like reward packets rather than distinct play styles. The bread-state high-chaos section has identity and decision hooks, but the ordinary political and League routes still rely on generic helper calls. Priority IDs:

- `ukr_soviet_collapse_question_of_statehood`
- `ukr_soviet_collapse_socialist_republic_without_moscow`
- `ukr_soviet_collapse_officers_above_parties`
- `ukr_soviet_collapse_elections_under_shellfire`
- `ukr_soviet_collapse_league_founding_charter`
- `ukr_soviet_collapse_border_states_accept_kyiv`
- `ukr_soviet_collapse_external_border_arbitration`
- `ukr_soviet_collapse_black_soil_oath`

Fix direction: give each route a persistent decision or mission surface and make the League/foreign routes choose between sponsor dependency, equal federation, or armed border settlement. Keep bread-state mechanics as the identity-specific benchmark.

### Belarus

Belarus has clear rail/corridor/forest identity, but the rail route is still under-differentiated. Several focuses unlock useful helpers without a visible rail-state loop comparable to PRA.

Priority IDs:

- `blr_soviet_collapse_the_rail_map_on_the_wall`
- `blr_soviet_collapse_which_road_is_belarus`
- `blr_soviet_collapse_eastern_line_watch`
- `blr_soviet_collapse_timetable_state`
- `blr_soviet_collapse_railway_neutrality`
- `blr_soviet_collapse_rail_war_state`

Fix direction: add rail-routing decisions, corridor tolls, evacuation/train missions, or armored train/supply line choices. The branch should decide whether Belarus is a neutral corridor, fortress transit state, or war logistics hub.

### Kazakhstan

Kazakhstan has the largest republic tree and many route concepts: Alash, socialist, resource directorate, southern league, steppe military, Karaganda/oil. The issue is layout sprawl plus too many route nodes resolving to generic helper payloads.

Priority IDs:

- `kaz_soviet_collapse_the_congress_chooses_a_past`
- `kaz_soviet_collapse_alash_memory_restored`
- `kaz_soviet_collapse_socialist_steppe_republic`
- `kaz_soviet_collapse_resource_defense_directorate`
- `kaz_soviet_collapse_resource_concessions_debate`
- `kaz_soviet_collapse_domestic_resource_state`
- `kaz_soviet_collapse_league_resource_pool`
- `kaz_soviet_collapse_foreign_technical_missions`
- `kaz_soviet_collapse_steppe_federation_charter`

Fix direction: turn the resource branch into a real resource-security/concession mechanic and the steppe federation branch into a southern league system with target states, patrol decisions, and postwar settlement. Separate the route layout into clearer columns.

### Regional Republics

Baltic, Caucasus, Central Asia, Moldova, internal republics, and generic breakaways have decent compact coverage but not enough route-specific postwar handling. Many focuses remain generic "legal recognition / security supply / league preparation" calls. Internal republics need special attention because one tree covers many tags; the tree should vary by tag flags or tag-specific payloads.

Priority groups:

- `soviet_collapse_internal_republic_focus_tree`
- `soviet_collapse_baltic_focus_tree`
- `soviet_collapse_caucasus_focus_tree`
- `soviet_collapse_central_asia_focus_tree`
- `soviet_collapse_moldova_focus_tree`
- `soviet_collapse_breakaway_focus_tree`

Fix direction: add tag-specific route branches or payloads for Crimea, Volga/Ural, Siberian/Far Eastern/Yakutia/Buryatia/Tuva cases. Regional compact trees should unlock local decisions, claims/cores with settlement, and league/faction consequences.

### Custom Chaos Countries

The custom splinter set is broad but uneven. The large 47-focus skeleton gives many tags depth on paper, but repeated helper calls flatten identity. High-chaos countries should be extremely overpowered and identity-specific; many are aggressive enough at endpoints but not distinct enough in midgame.

Priority identity checks:

- `PRA`: strongest identity-specific rail package. It has rail authority ideas, rail decisions, armored train/directorate choices, and moving-state concepts. Still watch authority idea churn through `soviet_collapse_update_pra_authority_idea`.
- `DSC`: strong concept with `DSC_congress_of_the_dead_army`, `dsc_convene_the_dead_army`, and `dsc_order_the_dead_army_forward`, but earlier nodes still use generic legal/security helpers. It should receive a dead-army campaign loop earlier.
- `NRF`: strong endpoint names and naval XP/dockyard/convoy rewards, but lacks a unique naval mission loop. Add fleet raising, ghost convoy, Arctic port, or raiding decisions.
- `FEV`: Far Eastern actor should be more aggressive and Pacific-border specific. Current branch has generic fort/security/war-plan rewards.
- `BSC`: Central Asian old-movement identity exists, but should get cavalry/irregular water-road mechanics and league tension.
- `BBH`: anarchist/Black Banner identity needs more irregular expansion and anti-state decisions, not only generic chaos assault helpers.
- `KRS`: naval council/sailor identity should have port/fleet/sailor soviet decisions.
- `SDZ`: sealed security authority needs archive/prison/intelligence mechanics instead of mostly generic security helpers.
- `TSC`, `RMC`, `ICD`: high-chaos myth/death states need stranger mechanics and more destructive payoff. Current 18-focus compact trees are too shallow for their concepts.
- `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`: 47-focus skeleton exists, but parent should audit one by one for actual unique branch mechanics rather than title-only identity.

### Factory Successors

CFR and MFR are the best candidates for "extremely overpowered and identity-specific" chaos-country trees, but they need better branch layout and less same-row mutual-exclusion clutter.

- `CFR`: construction/civilian factory directorate has a strong trunk and decision hooks (`cfr_survey_unfinished_sites`, `cfr_issue_reconstruction_contracts`) but should become a construction project system, not repeated construction reward packets. Fix same-row governance and strategy forks first.
- `MFR`: military factory successor is strong and appropriately overpowered at the late arsenal route. It should consolidate repeated arms-factory/equipment rewards into arsenal quota decisions and make proxy arming/foreign contracts more visible.
- `OGB`: 23 focuses is thin for a required future-event hook/restoration package. It has Volga legitimacy and river authority, but needs a stronger future Bulgaria bridge, religion/society branch, and regional rival/settlement content.

### Ancient Restorations

KZR/SOG/KHW/ALN are functional compact trees, but too shallow for high-chaos restorations. They should not become full 47-focus monsters, but each needs one defining mechanic:

- KZR: toll/transit authority and Caspian/Volga route decisions.
- SOG: city/trade-road diplomacy and merchant corridors.
- KHW: water/canal/irrigation authority and river basin settlement.
- ALN: pass/mountain oath defense, Caucasus road control, and neighbor settlement.

Currently, several focuses use large hidden bundles of flags, claims, variables, train/equipment/building rewards. That is better than visible spam, but the player still needs a reason to play the restoration differently.

## Top 10 Fastest High-Impact Fixes

1. `common/national_focus/005_soviet_collapse_factory_successors.txt`: move CFR same-row mutual exclusions off single rows. Patch `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`, then `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`.
2. `common/national_focus/005_soviet_collapse_republics.txt`: space Kazakhstan route fork around `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_socialist_steppe_republic`, `kaz_soviet_collapse_resource_defense_directorate`.
3. `common/national_focus/005_soviet_collapse_republics.txt`: widen Ukraine early/foreign path around `ukr_soviet_collapse_war_without_a_declaration`, `ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_black_sea_port_ledgers`.
4. `common/national_focus/005_soviet_collapse_republics.txt`: fix same-row Moldova mutual exclusion pathline around `moldova_soviet_collapse_conditional_union`, `moldova_soviet_collapse_alliance_not_union`, `moldova_soviet_collapse_reject_the_union_question`.
5. `common/national_focus/005_soviet_collapse_republics.txt`: fix same-row internal republic mutual exclusion around `internal_soviet_collapse_security_council`, `internal_soviet_collapse_legal_autonomy_congress`, `internal_soviet_collapse_border_and_rail_liaisons`.
6. `common/scripted_effects/005_soviet_collapse_effects.txt`: audit `soviet_collapse_clear_republic_staged_ideas` and ensure it is always hidden behind custom tooltips when focus-triggered.
7. `common/scripted_effects/005_soviet_collapse_effects.txt`: audit `soviet_collapse_add_republic_focus_recovery_progress` and prevent repeated visible disorder-spirit churn from common focus helpers.
8. `common/scripted_effects/005_soviet_collapse_effects.txt`: audit `soviet_collapse_update_pra_authority_idea` for repeated clear/add churn, then call it only from PRA route milestones that actually change authority state.
9. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: add one unique decision unlock to NRF mid-branch before `NRF_fleet_that_does_not_dock`.
10. `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: add one unique decision unlock or route-specific variable payoff to each ancient tree capstone, starting with `KZR_khazar_charter`, `SOG_sogdian_city_charter`, `KHW_khwarazmian_water_charter`, `ALN_expansionist_mountain_claims`.

## Top 10 Deep Route Rewrites Needed

1. CFR construction directorate: convert repeated construction rewards into a construction project mechanic and clarify governance/strategy forks.
2. Kazakhstan resource directorate and southern federation: resource security, concessions, league pool, and steppe federation should be a full political/economic system.
3. Belarus rail state: turn rail map/timetable/neutrality/war-state branch into a corridor and armored-train logistics system.
4. NRF naval death-state: add a fleet-raising, convoy, Arctic port, or naval raiding mission loop.
5. DSC dead soldiers/dead congress: move dead-army mechanics earlier and make living-memorial vs dead-army routes materially different.
6. OGB future Bulgaria/restoration: expand Volga legitimacy, religion/society, river authority, and future-event hook.
7. FEV Far Eastern authority: give it Pacific/Amur/Trans-Siberian border mechanics and aggressive regional war/settlement options.
8. SDZ sealed security zone: create archive/prison/intelligence mechanics and internal control payoffs.
9. Ancient restorations: give KZR/SOG/KHW/ALN one bespoke mechanic each and integrate with regional leagues/neighbors.
10. Generic 47-focus custom splinter skeleton: reduce title-only identity by adding tag-specific helper payloads for BSC, TNC, ALA, BBH, KRS, UDC, GAC, DHC, KHC, SZA, UWD, MRC, IUL, BAC, ARD, NLC.

## Commands and Key Outputs

Commands run:

```bash
sed -n '1,220p' .agents/skills/hoi4-focus-trees/SKILL.md
sed -n '1,220p' .agents/skills/chaos-redux-events/SKILL.md
sed -n '1,260p' .agents/skills/chaos-redux-subagents/SKILL.md
rg --files paradox_wiki | rg '((National focus|Focus|Effects|Triggers|Localisation|Scopes|AI modding|Modifiers|Decision modding|Data structures|Event modding|On actions|Idea modding).*Hearts of Iron 4 Wiki\\.md$)'
sed -n '1,220p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'
sed -n '220,520p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'
sed -n '1,120p' 'paradox_wiki/Effect - Hearts of Iron 4 Wiki.md'
rg -n 'focus|national_focus|mutually_exclusive|prerequisite|allow_branch|ai_will_do|path' ~/projects/Hearts\\ of\\ Iron\\ IV/documentation/*.md
rg -n '\\b(add_ideas|remove_ideas|swap_ideas|add_timed_idea|modify_ideas|add_dynamic_modifier|remove_dynamic_modifier)\\b' common/national_focus/005_soviet_collapse_*.txt common/scripted_effects common/ideas/005_soviet_collapse_ideas.txt
python3 - <<'PY'
# read-only corrected Clausewitz focus parser for counts, reward patterns, and coordinate/pathline heuristics
PY
```

Key parser output:

```text
tree_count 41 focus_count 1698
005_soviet_collapse_republics.txt 9 501
005_soviet_collapse_custom_splinters.txt 25 1005
005_soviet_collapse_factory_successors.txt 3 128
005_soviet_collapse_ancient_restorations.txt 4 64
direct_idea_focus_count 0
layout_totals duplicate_positions tight_adjacent parent_geometry_risks same_row_mutex_risks 0 883 223 114
generic_apply_focus_helper_calls_top:
soviet_collapse_apply_focus_depot_and_supply_control 138
soviet_collapse_apply_focus_military_consolidation 131
soviet_collapse_apply_focus_legal_recognition 107
soviet_collapse_apply_focus_republican_compact_plan 96
```

## Machine-Readable Appendix

CSV-style rows:

```csv
file,tree_id,focus_id,issue_type,severity,evidence,proposed_fix
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_elect_the_site_committees,layout_mutex_pathline,high,"same-row governance mutex at y=6 with other governance siblings","move mutually exclusive choices into staggered fork columns or add vertical spacing"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_publish_the_planners_charter,layout_mutex_pathline,high,"same-row governance mutex at y=6","stagger governance branch and avoid red line through sibling focuses"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_invite_the_foreign_contract_board,layout_mutex_pathline,high,"same-row governance mutex at y=6","stagger governance branch and add route-specific construction-contract payoff"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_the_concrete_committee,layout_mutex_pathline,high,"same-row governance mutex at y=6","stagger governance branch and make coercive-build route visually separate"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_cities_first,layout_mutex_pathline,high,"same-row construction strategy mutex at y=9","separate cities/rails/factories/contracts strategy choices"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_rails_first,layout_mutex_pathline,high,"same-row construction strategy mutex at y=9","separate strategy choices and add rail-project decision"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_factories_first,layout_mutex_pathline,high,"same-row construction strategy mutex at y=9","separate strategy choices and add factory-project decision"
common/national_focus/005_soviet_collapse_factory_successors.txt,CFR_soviet_collapse_focus_tree,CFR_contracts_first,layout_mutex_pathline,high,"same-row construction strategy mutex at y=9","separate strategy choices and add contract-board consequence"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_kazakhstan_focus_tree,kaz_soviet_collapse_the_congress_chooses_a_past,layout_branch_sprawl,high,"Kazakhstan tree has 72 tight pairs and 24 prerequisite geometry risks","rebuild route fork columns before reward rewrite"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_kazakhstan_focus_tree,kaz_soviet_collapse_alash_memory_restored,route_depth,high,"route starts with generic legal recognition helper","add Alash court/constitution/advisor/decision chain"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_kazakhstan_focus_tree,kaz_soviet_collapse_socialist_steppe_republic,route_depth,medium,"route starts with generic socialist sovereignty helper","add soviet-steppe supply plan and ruling-party/decision changes"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_kazakhstan_focus_tree,kaz_soviet_collapse_resource_defense_directorate,route_depth,high,"resource route begins with security supply helper plus variable","build resource-security/concession decision family"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_kazakhstan_focus_tree,kaz_soviet_collapse_resource_concessions_debate,route_depth,high,"resource fork exists but needs stronger consequences","make domestic/league/foreign concessions change decisions and patron risk"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_ukraine_focus_tree,ukr_soviet_collapse_war_without_a_declaration,layout_tight,medium,"tight with liaison/Black Sea nodes around x=25 y=4-5","widen early war/foreign lanes"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_ukraine_focus_tree,ukr_soviet_collapse_league_founding_charter,route_depth,high,"League route should be major Ukraine payoff","tie to league decisions, member obligations, and border settlement"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_ukraine_focus_tree,ukr_soviet_collapse_border_states_accept_kyiv,route_depth,high,"expansion/league payoff currently helper-heavy","add protectorate/federation/postwar integration choices"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_ukraine_focus_tree,ukr_soviet_collapse_black_soil_oath,route_depth,medium,"bread-state route is identity-specific but should remain benchmark","ensure decision hooks are visible and not only spirit/stat rewards"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_belarus_focus_tree,blr_soviet_collapse_the_rail_map_on_the_wall,route_depth,high,"rail branch begins with helper payload only","add rail map/corridor decision loop"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_belarus_focus_tree,blr_soviet_collapse_timetable_state,route_depth,high,"rail-state identity not yet comparable to PRA","add train timetable/corridor toll/armored train mechanics"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_belarus_focus_tree,blr_soviet_collapse_railway_neutrality,route_depth,medium,"finisher needs distinct neutral-corridor consequence","add neutrality guarantees and corridor settlement decisions"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_belarus_focus_tree,blr_soviet_collapse_rail_war_state,route_depth,medium,"finisher needs distinct war-logistics consequence","add supply train, armored train, and war-prep missions"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_moldova_focus_tree,moldova_soviet_collapse_alliance_not_union,layout_mutex_pathline,medium,"focus sits between mutually exclusive conditional/reject union focuses","stagger Romania question branch"
common/national_focus/005_soviet_collapse_republics.txt,soviet_collapse_internal_republic_focus_tree,internal_soviet_collapse_legal_autonomy_congress,layout_mutex_pathline,medium,"sits between mutually exclusive security/rail choices","stagger internal republic authority fork"
common/national_focus/005_soviet_collapse_custom_splinters.txt,PRA_soviet_collapse_focus_tree,PRA_the_timetable_declares_authority,idea_lifecycle,medium,"calls PRA authority updater from first node","verify authority idea changes only at real route milestones"
common/national_focus/005_soviet_collapse_custom_splinters.txt,PRA_soviet_collapse_focus_tree,PRA_armored_train_directorate,idea_lifecycle,medium,"calls rail authority reward and PRA authority updater","keep idea replacement hidden and route-specific"
common/national_focus/005_soviet_collapse_custom_splinters.txt,DSC_soviet_collapse_focus_tree,DSC_congress_of_the_dead_army,route_depth,high,"strong endpoint but dead-army mechanic arrives late","move dead army decisions and mobilisation earlier"
common/national_focus/005_soviet_collapse_custom_splinters.txt,DSC_soviet_collapse_focus_tree,DSC_memorial_frontier_state,route_depth,medium,"living/memorial route needs distinct gameplay from dead army route","add memorial frontier defense/recruitment decisions"
common/national_focus/005_soviet_collapse_custom_splinters.txt,NRF_soviet_collapse_focus_tree,NRF_fleet_that_does_not_dock,route_depth,high,"naval endpoint is strong but mid-branch lacks unique loop","add revenant fleet/ghost convoy/naval raid mission family"
common/national_focus/005_soviet_collapse_custom_splinters.txt,NRF_soviet_collapse_focus_tree,NRF_northern_revenant_fleet,route_depth,high,"should be extremely overpowered naval chaos payoff","add fleet spawn or port seizure mechanic with AI aggression"
common/national_focus/005_soviet_collapse_custom_splinters.txt,FEV_soviet_collapse_focus_tree,FEV_war_plan,route_depth,high,"Far East route reads as generic war/security helper","add Amur/Pacific/Trans-Siberian war and settlement system"
common/national_focus/005_soviet_collapse_custom_splinters.txt,SDZ_soviet_collapse_focus_tree,SDZ_informant_cipher_schools,route_depth,high,"security state needs archive/intelligence mechanics","add prison/archive/informant decision loop"
common/national_focus/005_soviet_collapse_custom_splinters.txt,BSC_soviet_collapse_focus_tree,BSC_caravan_officer_schools,route_depth,medium,"Basmachi identity needs more than generic assault helper","add cavalry/irregular/water-road decisions"
common/national_focus/005_soviet_collapse_custom_splinters.txt,KRS_soviet_collapse_focus_tree,KRS_sailor_soviet_path,route_depth,medium,"sailor state should have port/fleet mechanics","add naval council or port seizure decisions"
common/national_focus/005_soviet_collapse_factory_successors.txt,OGB_soviet_collapse_focus_tree,OGB_future_bulgaria_file,route_depth,high,"future-event hook exists but route is only 23 focuses","expand future Bulgaria bridge and Volga restoration decisions"
common/national_focus/005_soviet_collapse_factory_successors.txt,MFR_soviet_collapse_focus_tree,MFR_eternal_arsenal_marches,reward_design,medium,"appropriately overpowered but repeats direct AI/building/equipment payloads","consolidate into arsenal-state helper and decision loop"
common/national_focus/005_soviet_collapse_factory_successors.txt,MFR_soviet_collapse_focus_tree,MFR_no_peace_without_orders,reward_design,medium,"neighbor-wide wargoal loop is powerful but hidden in focus reward","move to documented arsenal war-plan helper with tooltip"
common/national_focus/005_soviet_collapse_ancient_restorations.txt,KZR_soviet_collapse_ancient_focus_tree,KZR_khazar_charter,route_depth,medium,"large hidden bundle but limited bespoke gameplay","add toll/transit authority decision payoff"
common/national_focus/005_soviet_collapse_ancient_restorations.txt,SOG_soviet_collapse_ancient_focus_tree,SOG_sogdian_city_charter,route_depth,medium,"ancient restoration compact tree needs unique trade mechanic","add merchant-road/city diplomacy decisions"
common/national_focus/005_soviet_collapse_ancient_restorations.txt,KHW_soviet_collapse_ancient_focus_tree,KHW_khwarazmian_water_charter,route_depth,medium,"ancient restoration compact tree needs unique water mechanic","add canal/irrigation/water settlement decisions"
common/national_focus/005_soviet_collapse_ancient_restorations.txt,ALN_soviet_collapse_ancient_focus_tree,ALN_expansionist_mountain_claims,route_depth,medium,"mountain restoration needs pass-control mechanic","add Caucasus pass oath/road-control decisions"
common/scripted_effects/005_soviet_collapse_effects.txt,shared,soviet_collapse_clear_republic_staged_ideas,idea_lifecycle,high,"96 direct idea tokens in cleanup helper","keep hidden and replace mass cleanup with staged upgrade helper"
common/scripted_effects/005_soviet_collapse_effects.txt,shared,soviet_collapse_update_pra_authority_idea,idea_lifecycle,medium,"clears and re-adds PRA authority ideas by focus flags","call only when authority tier actually changes"
common/scripted_effects/005_soviet_collapse_effects.txt,shared,soviet_collapse_add_republic_focus_recovery_progress,idea_lifecycle,medium,"common helper can mutate startup disorder ideas through many focus routes","ensure no visible tooltip spam and no repeated no-op churn"
```

## Completion Boundary

This is a subagent audit handoff only. It does not claim completion of the parent Event005 rework.
