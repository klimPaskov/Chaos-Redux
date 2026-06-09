# Event005 Soviet Collapse Focus Tree Full Analysis and Tranche Plan

Date: 2026-06-01

Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No gameplay patch was made. The remaining problems are broad route architecture, reward architecture, branch payoff, and layout work. A small local patch would not address the user's current objective.

Do-not-touch constraint honored: this pass did not edit `gfx/flags`, flag sprite files, `interface/flags`, or any `gfx` or `interface` file.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.
- Event005 specs/docs: `docs/events/005_soviet_collapse.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.

## Machine Counts

| Metric | Count |
|---|---:|
| Scoped files | 4 |
| Focus trees | 41 |
| Focus ids | 1,698 |
| Unique focus ids | 1,698 |
| Duplicate focus ids | 0 |
| Focuses with direct `add_ideas` | 0 |
| Direct `add_ideas` occurrences | 0 |
| Focuses with the same direct idea repeated in the focus | 0 |
| Direct idea ids repeated across focuses | 0 |
| Focuses with 2+ direct `add_ideas` | 0 |
| Focuses with direct stockpile reward | 170 |
| Direct stockpile reward occurrences | 170 |
| Focuses with 2+ direct stockpile effects | 0 |
| Missing `ai_will_do` | 0 |
| Missing `search_filters` | 0 |
| Missing focus icon assignments | 0 |
| Missing focus title localisation | 0 |
| Missing focus description localisation | 0 |
| Same-coordinate focus groups | 0 |
| Parser-detected same-row mutual-exclusion span risks | 15 |
| Non-downward same-tree prerequisites | 0 |

Direct focus idea spam is currently cleared. The remaining "idea spam" complaint maps to older setup/decision/helper surfaces and the play feel caused by repeated helper buckets, not direct focus `add_ideas` in the four scoped files.

Top repeated focus helper calls in rewards:

| Helper | Calls |
|---|---:|
| `soviet_collapse_apply_focus_depot_and_supply_control` | 138 |
| `soviet_collapse_apply_focus_military_consolidation` | 132 |
| `soviet_collapse_apply_focus_legal_recognition` | 117 |
| `soviet_collapse_apply_focus_republican_compact_plan` | 80 |
| `soviet_collapse_apply_focus_foreign_channel` | 63 |
| `soviet_collapse_apply_focus_high_chaos_identity` | 60 |
| `soviet_collapse_apply_focus_security_supply_plan` | 57 |
| `soviet_collapse_apply_focus_league_preparation` | 52 |
| `soviet_collapse_apply_focus_foreign_recognition_plan` | 37 |
| `soviet_collapse_apply_focus_foreign_league_plan` | 29 |
| `soviet_collapse_apply_focus_chaos_assault_plan` | 28 |
| `soviet_collapse_apply_focus_socialist_sovereignty` | 23 |

## Route Coverage Table

| Tree | Focuses | Direct wargoal | Claims | Aggressive AI focus | Coverage judgment |
|---|---:|---:|---:|---:|---|
| `soviet_collapse_ukraine_focus_tree` | 83 | 0 | 0 | 0 | Large branch count but visually tangled; expansion largely decision/helper mediated rather than direct. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 0 | 0 | Moderate shared breakaway tree; still generic. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 0 | 0 | Broad internal-republic coverage; lacks direct expansion and distinct regional mechanics. |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 0 | 0 | Playable regional tree; legal/league path exists but expansion pressure is weak. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 0 | 0 | 0 | Mountain/oil framing exists; needs more state and border mechanics. |
| `soviet_collapse_central_asia_focus_tree` | 45 | 0 | 1 | 0 | Regional coverage exists; cotton/water/rail loops need decisions and stronger payoffs. |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 0 | 0 | Corridor and Romanian diplomacy exist; expansion/diplomacy payoffs remain light. |
| `soviet_collapse_belarus_focus_tree` | 53 | 0 | 0 | 0 | Real rail/forest/corridor tree; pathlines are still a major readability risk. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 0 | 0 | 0 | Largest republic tree; good route surface but still helper-heavy and under-aggressive. |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 0 | 0 | Template-sized custom tree; not enough identity-specific mechanics. |
| `PRA_soviet_collapse_focus_tree` | 22 | 1 | 0 | 1 | Compact rail-state identity; too short and too stockpile/building heavy. |
| `TSC_soviet_collapse_focus_tree` | 18 | 1 | 0 | 1 | Shallow special tree; science/star identity lacks a living mechanic. |
| `RMC_soviet_collapse_focus_tree` | 18 | 1 | 0 | 1 | Shallow special tree; reliquary/dead-volunteer identity is underbuilt. |
| `DSC_soviet_collapse_focus_tree` | 18 | 1 | 0 | 4 | Mechanized through decisions, but focus tree remains too compressed. |
| `NRF_soviet_collapse_focus_tree` | 18 | 1 | 0 | 3 | Naval revenant identity exists but needs naval/port/dockyard branch depth. |
| `ICD_soviet_collapse_focus_tree` | 18 | 1 | 0 | 1 | Shallow death-commissariat tree; needs coercive politics and expansion loop. |
| `BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC` | 47 each | 0 each | 0 each | 0 each | Template-sized route trees; many still read as reward-template variants. |
| `CFR_soviet_collapse_focus_tree` | 47 | 2 | 0 | 2 | Best construction-state surface, but single-building rewards and hidden route locks remain. |
| `OGB_soviet_collapse_focus_tree` | 23 | 2 | 1 | 2 | Compact restoration tree; too shallow for a high-chaos/special successor. |
| `MFR_soviet_collapse_focus_tree` | 58 | 1 | 0 | 3 | Stronger factory tree; still needs route payoff polish. |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 1 | 3 | 1 | Stub-depth ancient restoration. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 1 | 3 | 1 | Stub-depth ancient restoration. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 1 | 3 | 1 | Stub-depth ancient restoration. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | 1 | 3 | 1 | Stub-depth ancient restoration. |

Spec mismatch: Part 5 requires political, industry, and expansion branches for every playable/long-lived tree, plus military/diplomacy/special branches for major countries. The four ancient trees, `TSC/RMC/DSC/NRF/ICD`, `PRA`, and `OGB` do not meet that depth standard. Large republic trees meet branch count better, but Ukraine, Belarus, Kazakhstan, and shared regional trees still lack direct expansion/aggression surfaces and route-specific mechanics at the level promised by the spec.

## Missing or Simplified Content

High-priority issues first:

1. `005_soviet_collapse_ancient_restorations.txt`: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, and `ALN_soviet_collapse_ancient_focus_tree` are 16-focus stubs. They need restoration politics, state economy, military order, diplomacy, expansion, and postwar identity mechanics.
2. `005_soviet_collapse_custom_splinters.txt`: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree` are 18 focuses each; `PRA_soviet_collapse_focus_tree` is 22. They do not satisfy the "chaos countries should be overpowered and identity-specific" target.
3. `005_soviet_collapse_factory_successors.txt`: `OGB_soviet_collapse_focus_tree` has 23 focuses and remains compact; it needs Volga trade/restored-name mechanics or a clear reason to stay narrow.
4. `005_soviet_collapse_republics.txt`: `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, and `soviet_collapse_kazakhstan_focus_tree` have enough focuses, but too many rewards collapse into shared helper buckets.
5. `005_soviet_collapse_custom_splinters.txt`: 18 template-sized 47-focus custom splinters have branch labels but little direct war/claim/core behavior. They need identity mechanics, not only renamed versions of `first_guard`, `stores`, `legitimacy`, `war_plan`, `diplomatic_plan`, `settlement`, `industry_plan`, `hidden_doctrine`, and `endgame`.
6. All four files: direct focus idea stacking is gone, but repeated helpers still flatten country identity. The top four helpers alone account for 467 focus reward calls.
7. All four files: only 16 focuses directly provide wargoals or claims across 1,698 focuses. For the requested overpowered chaos-country behavior, aggression is too indirect.

## Icon Coverage Table

| File | Focuses | Missing icons | Unique icon ids | Repeated icon ids | Top repeat examples |
|---|---:|---:|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 501 | 0 | 458 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_moldova_soviet_collapse_ukrainian_corridor` |
| `005_soviet_collapse_custom_splinters.txt` | 1,005 | 0 | 885 | 99 | `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, `GFX_focus_IUL_war_plan` |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 113 | 11 | `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_civilian_hegemony_project` |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 42 | 8 | `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state` |

No `.gfx` or sprite files were edited or inspected for patching. Icon wiring appears syntactically present from the focus files, but repeated icon ids reinforce the generic-template feeling.

## Localisation and Reward Mismatches

Mechanical localisation coverage is complete for focus names and descriptions: 0 missing names, 0 missing descriptions.

Reward mismatch risks:

| File | Focus ids | Issue |
|---|---|---|
| `005_soviet_collapse_custom_splinters.txt` | `PRA_the_pale_line_endures`, `PRA_charge_for_safe_passage`, `PRA_armored_train_schools`, `PRA_the_board_overrules_ministers` | Rail-sovereignty text still resolves too often as train stockpiles, buildings, or generic helpers. |
| `005_soviet_collapse_custom_splinters.txt` | `NRF_fleet_that_does_not_dock`, `NRF_port_republic_of_the_living`, `NRF_count_the_drowned_crews`, `NRF_living_harbor_committees`, `NRF_claim_the_white_sea_lane` | Revenant fleet text promises naval authority; rewards still lean on stockpiles/helper or lack direct naval expansion. |
| `005_soviet_collapse_custom_splinters.txt` | `DSC_voronezh_rearguard_archives`, `DSC_field_hospital_memorials`, `DSC_rearguard_supply_bureau` | Dead-soldier identity is stronger than the direct reward payload. |
| `005_soviet_collapse_custom_splinters.txt` | `TSC_portable_laboratory_trains`, `TSC_perimeter_regiments` | Tunguska/science identity needs special mechanics or projects, not stockpile/building rewards. |
| `005_soviet_collapse_custom_splinters.txt` | `RMC_lipetsk_reliquary_workshops`, `RMC_blood_oath_requisitions`, `RMC_dead_volunteer_columns`, `RMC_claim_the_burial_roads` | Reliquary/dead-volunteer concepts are implemented as ordinary factories/equipment/helper rewards. |
| `005_soviet_collapse_custom_splinters.txt` | `ICD_penza_memorial_workshops`, `ICD_black_seal_requisitions`, `ICD_memorial_battalions`, `ICD_claim_the_unburied_front` | Death-commissariat route needs coercion/repression/front mechanics. |
| `005_soviet_collapse_factory_successors.txt` | `CFR_the_trust_office_takes_the_seal`, `CFR_emergency_cement_accounts`, `CFR_the_first_new_district`, `CFR_a_civilian_factory_in_every_capital`, `CFR_the_state_that_builds`, `CFR_rebuild_russia_without_moscow` | Construction-state text should feed mandates, site registry, protectorate/rebuild systems, claims, or integration, not mostly one-building rewards. |
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_returned_names_endgame`, `SOG_returned_names_endgame`, `KHW_returned_names_endgame`, `ALN_returned_names_endgame` | Endgame names imply restored-state payoff, but rewards are still compact/helper-led. |
| `005_soviet_collapse_republics.txt` | `internal_soviet_collapse_northern_timber_rail_fund`, `internal_soviet_collapse_ural_cavalry_roads`, `central_asia_soviet_collapse_turkestan_city_congress`, `kaz_soviet_collapse_turkmen_rail_and_desert_talks` | Regional branch names are specific, but rewards still combine one building with generic helper calls. |

## Top 30 Weak Reward Candidates

Machine-scored from live focus blocks. Reasons include shallow-tree membership, direct stockpile reward, stockpile without direct system/war unlock, single-building-only reward, multiple generic helpers, annexation filter without direct expansion, and identity title with weak direct payoff.

| Score | File | Tree | Focus id | Reason |
|---:|---|---|---|---|
| 19 | `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | `PRA_the_pale_line_endures` | shallow tree; stockpile; multiple helpers; weak rail-state payoff |
| 16 | `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | `NRF_fleet_that_does_not_dock` | shallow tree; single building; annexation filter lacks direct expansion |
| 15 | `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | `central_asia_soviet_collapse_desert_republic_settlement` | stockpile plus multiple helpers |
| 14 | `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | `KZR_khazar_charter` | shallow tree; stockpile; annexation-filter mismatch risk |
| 14 | `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | `KZR_returned_names_endgame` | shallow tree; helper-only identity payoff |
| 14 | `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | `SOG_returned_names_endgame` | shallow tree; helper-only identity payoff |
| 14 | `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | `KHW_khwarazmian_water_charter` | shallow tree; stockpile; annexation-filter mismatch risk |
| 14 | `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | `KHW_returned_names_endgame` | shallow tree; helper-only identity payoff |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | `PRA_charge_for_safe_passage` | shallow tree; stockpile; building-list reward |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | `TSC_portable_laboratory_trains` | shallow tree; stockpile without direct system unlock |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | `TSC_perimeter_regiments` | shallow tree; stockpile and buildings |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | `NRF_port_republic_of_the_living` | shallow tree; stockpile; weak naval payoff |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `IUL_soviet_collapse_focus_tree` | `IUL_volga_ural_endurance` | single building plus multiple helpers |
| 14 | `005_soviet_collapse_custom_splinters.txt` | `BAC_soviet_collapse_focus_tree` | `BAC_amur_commune_endurance` | single building plus multiple helpers |
| 14 | `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | `internal_soviet_collapse_northern_timber_rail_fund` | single building plus multiple helpers |
| 14 | `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | `internal_soviet_collapse_ural_cavalry_roads` | single building plus multiple helpers |
| 14 | `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | `central_asia_soviet_collapse_turkestan_city_congress` | single building plus multiple helpers |
| 14 | `005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | `kaz_soviet_collapse_turkmen_rail_and_desert_talks` | single building plus multiple helpers |
| 12 | `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | `KHW_canal_recognition_letters` | shallow tree; stockpile without direct system unlock |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | `PRA_the_board_overrules_ministers` | shallow tree; stockpile plus helper |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | `PRA_armored_train_schools` | shallow tree; stockpile without direct rail-system unlock |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | `RMC_lipetsk_reliquary_workshops` | shallow tree; stockpile and building |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | `RMC_blood_oath_requisitions` | shallow tree; stockpile and building |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | `RMC_dead_volunteer_columns` | shallow tree; stockpile and building |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | `RMC_claim_the_burial_roads` | shallow tree; annexation filter lacks direct expansion |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | `RMC_procession_columns` | shallow tree; annexation filter lacks direct expansion |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | `DSC_voronezh_rearguard_archives` | shallow tree; stockpile plus helper |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | `DSC_field_hospital_memorials` | shallow tree; stockpile plus helper |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | `NRF_count_the_drowned_crews` | shallow tree; stockpile plus helper |
| 12 | `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | `NRF_living_harbor_committees` | shallow tree; stockpile without direct naval-system unlock |

## Pathline and Mutual-Exclusion Risks

Parser-detected same-row mutual-exclusion span risks:

| File | Tree | Focus pair | Intervening focuses |
|---|---|---|---|
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | `baltic_soviet_collapse_legal_continuity_government` / `baltic_soviet_collapse_military_border_government` | `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council`, `baltic_soviet_collapse_singing_barricades_early` |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | `baltic_soviet_collapse_baltic_league_first` / `baltic_soviet_collapse_foreign_protection_council` | `baltic_soviet_collapse_singing_barricades_early` |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_alliance_not_union` / `moldova_soviet_collapse_conditional_union` | `moldova_soviet_collapse_smugglers_and_border_committees` |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | `moldova_soviet_collapse_alliance_not_union` / `moldova_soviet_collapse_reject_the_union_question` | `moldova_soviet_collapse_black_soil_recovery_boards` |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_military_transit_directorate` / `blr_soviet_collapse_national_council_of_minsk` | `blr_soviet_collapse_socialist_autonomy_without_moscow` |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | `blr_soviet_collapse_foreign_corridor_administration` / `blr_soviet_collapse_national_council_of_minsk` | `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate` |
| `005_soviet_collapse_custom_splinters.txt` | `UDC_soviet_collapse_focus_tree` | `UDC_radical_turn` / `UDC_settlement` | `UDC_loyalist_statute_guarantees` |
| `005_soviet_collapse_custom_splinters.txt` | `SDZ_soviet_collapse_focus_tree` | `SDZ_radical_turn` / `SDZ_settlement` | `SDZ_chain_of_custody_statutes` |
| `005_soviet_collapse_custom_splinters.txt` | `GAC_soviet_collapse_focus_tree` | `GAC_radical_turn` / `GAC_settlement` | `GAC_harvest_truce_guarantees` |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_soviet_collapse_focus_tree` | `DHC_radical_turn` / `DHC_settlement` | `DHC_convoy_autonomy_guarantees` |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_soviet_collapse_focus_tree` | `KHC_radical_turn` / `KHC_settlement` | `KHC_grain_passage_guarantees` |

Manual layout risk not fully captured by the parser: Ukraine and Belarus have long prerequisite spans across wide rows. These should be checked with screenshots after movement because the wiki warns duplicate and badly placed prerequisite lines can render path sprites badly, and route-lock arrows through choice clusters are visually ugly even when syntactically valid.

## AI Behavior Gaps

- Every focus has an `ai_will_do`, but many weights are flat base values or simple route-flag modifiers.
- `005_soviet_collapse_republics.txt`: there are 0 direct aggressive AI strategy focuses across 501 focuses. Ukraine, Belarus, Kazakhstan, and shared regional republics need AI priorities for expansion, league votes, patron dependence, border settlements, and anti-Soviet or neighbor wars.
- `005_soviet_collapse_custom_splinters.txt`: only 11 focuses add aggressive AI strategy across 1,005 focuses. Most 47-focus custom splinters have 0 direct wargoal, claim, or aggressive AI focuses.
- `005_soviet_collapse_factory_successors.txt`: CFR/MFR/OGB have better direct aggression than most trees, but `OGB` remains shallow and CFR strategy/governance route visibility is weak.
- `005_soviet_collapse_ancient_restorations.txt`: each ancient tree has one aggressive endpoint, but no strategic AI arc before that endpoint.

## Next 10 Parent Implementation Tranches

1. Ancient restoration expansion tranche: deepen `KZR/SOG/KHW/ALN` into real restoration route families with politics, old-border claims, state economy, military order, diplomacy, expansion, and postwar integration. Do not create new formable chains unless explicitly approved.
2. Special shallow chaos tranche: expand `TSC/RMC/DSC/NRF/ICD` and `PRA` from 18-22 focus compact trees into overpowered identity trees. Prioritize mechanics over focus count: rail authority, revenant fleet, dead army, laboratory/star pressure, reliquary processions, death commissariat.
3. OGB restoration tranche: expand `OGB_soviet_collapse_focus_tree` beyond 23 focuses or document a hard design reason for compactness; add Volga trade, restored-name legitimacy, old-border diplomacy, and direct expansion/integration payoffs.
4. Ukraine layout and route payoff tranche: untangle long route lines, keep only lore-important mutual exclusions visible, and convert route endpoints into distinct governments, League/Black Sea decisions, old-movement consequences, and aggressive/high-chaos behavior.
5. Belarus route-layout tranche: separate rail, forest, corridor, and League branches so prerequisites do not span unrelated columns; add route-specific rail/forest/corridor decisions and AI behavior.
6. Kazakhstan route payoff tranche: reduce helper reliance in the 92-focus tree; make Alash, socialist, military district, resource board, Central Asian League, foreign mediation, and high-chaos steppe routes alter decisions, claims, units, and AI.
7. Shared regional republic tranche: split internal, Baltic, Caucasus, Central Asia, Moldova, and generic breakaway trees into real regional mechanics with settlement, border, league, and economy loops; cut one-building-only rewards.
8. Template splinter mechanics tranche: pick the 10 worst 47-focus templates first (`ARD`, `KHC`, `UWD`, `DHC`, `FEV`, `BSC`, `BAC`, `IUL`, `NLC`, `KRS`) and replace stockpile/helper rewards with identity mechanics, claims/cores, units/templates, decisions, and aggressive AI.
9. Focus layout/mutual-exclusion tranche: after reward changes, move all same-row mutual-exclusion span risks listed above; mutual exclusives should mark identity-defining forks only, not decorative or convenience choices.
10. Icon and validation tranche: after focus ids/routes settle, route icon duplicates to the asset workflow without touching flags; rerun focus count, duplicate id, localisation, filter/reward, icon, layout, unsupported operator, and flag-path diff checks.

## Validation Run

- Parsed all four scoped focus files for focus-tree/focus counts, duplicate focus ids, icons, search filters, AI blocks, direct `add_ideas`, direct stockpiles, helper calls, claims/wargoals, and pathline coordinate risks.
- Localisation scan against `localisation/english/005_soviet_collapse*.yml`: 0 missing focus title keys, 0 missing focus description keys.
- Direct idea scan in four scoped focus files: 0 direct `add_ideas`, 0 direct `add_timed_idea`.
- Direct focus helper idea-lifecycle scan in `common/scripted_effects/005_soviet_collapse_effects.txt`: no `soviet_collapse_apply_focus_*` helper directly adds ideas.
- Flag-path validation before writing this handoff: scoped focus file list contained no `gfx/flags`, flag sprite, or `interface/flags` paths.

## Skipped Validation

- No in-game launch or focus tree screenshot validation was run.
- No `.gfx` or sprite definition audit was performed because the user explicitly forbade touching flags and this pass did not need asset inspection.
- No code patch was attempted because the remaining problems are broad redesign work.

## Remaining Route Risks

Event005 is not focus-tree complete. The current live focus files have valid surface wiring, but they still fail the full quality target in depth, identity-specific chaos power, direct aggression, route consequence, and layout readability.
