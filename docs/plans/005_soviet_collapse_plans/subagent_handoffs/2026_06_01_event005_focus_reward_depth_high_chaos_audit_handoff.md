# Event005 Focus Reward Depth And High-Chaos Audit Handoff

Date: 2026-06-01

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard constraint followed: no flag assets, no `gfx/flags`, no `interface/flags`, and no flag sprite/orientation logic were edited or inspected for changes.

## Summary

I audited current focus state for reward spam, branch depth, high-chaos payoff, layout/pathline risk, icons, localisation, and AI behavior. I did not patch focus files because the parser found no exact duplicate reward/helper calls inside a single focus and the remaining issues are broader than safe subagent patch scope.

Current parsed focus count is 1,698 focuses in 40 focus trees:

- Republic trees: 501 focuses.
- Custom splinter trees: 1,012 focuses.
- Factory successor trees: 128 focuses.
- Ancient restoration trees: 64 focuses.

Surface coverage is mechanically complete at the key level:

- Missing focus ids: 0.
- Duplicate focus ids: 0.
- Missing `icon`: 0.
- Missing `search_filters`: 0.
- Missing `completion_reward`: 0.
- Missing `ai_will_do`: 0.
- Missing focus localisation name keys: 0.
- Missing focus localisation `_desc` keys: 0.
- Missing focus icon sprite definitions, scanning repo and vanilla interface `.gfx` while excluding flag paths: 0.

## Route Coverage Table

| Required route family | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine emergency survival | `ukr_soviet_collapse_emergency_rada`, ministry/depot/rail/military early trunk | Present but stretched | Strong count and themes, but several payoffs still route-variable/helper driven. |
| Ukraine democratic Rada republic | `ukr_soviet_collapse_restore_the_central_rada_memory` through constitutional focuses | Present, needs payoff | Political text promises institutions; rewards lean on legal-recognition helpers and need leader/advisor/law/decision consequences. |
| Ukraine sovereign socialist republic | `ukr_soviet_collapse_soviets_without_moscow` route | Present, needs distinction | Needs clearer divergence from democratic/legal state beyond variables and generic sovereignty helpers. |
| Ukraine military directory | `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_the_directory_state` | Present, underpaid | `ukr_soviet_collapse_the_directory_state` at `005_soviet_collapse_republics.txt:722` still lacks direct officer, unit, law, or command payoff. |
| Ukraine grain/industry/Bread State | grain ledger, Black Banner, Bread State/high-chaos route | Present, partly strong | Bread decisions exist; late focuses should expose stronger decision unlocks and local-map consequences. |
| Ukraine Dnieper/Donbas/Black Sea | Dnieper, Donbas, Black Sea/port branch | Present, payoff mismatch | `ukr_soviet_collapse_black_sea_port_ledgers` around `005_soviet_collapse_republics.txt:1228` needs direct naval base/dockyard/convoy/coastal or Black Sea diplomacy hooks. |
| Belarus emergency/legal/rail/forest/corridor/League | `soviet_collapse_belarus_focus_tree` | Present, layout risk | `blr_soviet_collapse_partisans_or_army` around `:9637` lacks units/templates/missions; rail/forest/corridor lines have long pathline spans. |
| Kazakhstan emergency/Alash/socialist/military/resource/League/foreign/high-chaos | `soviet_collapse_kazakhstan_focus_tree` | Present, too wide | 92 focuses and unique icons, but key branches use helper stacks where state-targeted oil, rail, cavalry, airstrip, and border mechanics should carry more. |
| Baltic legal/coast/forest/recognition/League/anti-puppet | `soviet_collapse_baltic_focus_tree` | Present, layout risk | Political fork spans are wide; icon repeats remain. |
| Caucasus council/defense/oil/mediation/League/loyalists/high-chaos | `soviet_collapse_caucasus_focus_tree` | Present, route payoff uneven | Oil route has several long pathlines; oilfield/directorate focuses should get more direct resource, supply, and regional diplomacy surfaces. |
| Central Asian council/defense/Basmachi/foreign/economy/League/high-chaos | `soviet_collapse_central_asia_focus_tree` | Present, route payoff uneven | Resource/water/pass/rail themes exist but need more concrete state-targeted mechanics and fewer reused icon families. |
| Moldova council/Dniester/Romania/Ukraine/agrarian/river/League/high-chaos | `soviet_collapse_moldova_focus_tree` | Present, route payoff uneven | Good thematic coverage, but Romanian/union fork and bridge focuses need clearer direct diplomatic or border-settlement mechanics. |
| Internal republic compact crisis/local defense/economy/logistics/foreign/League/special | `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_breakaway_focus_tree` | Present, generic | Compact trees cover the minimum but still often read as shared helper progression rather than adapted local identity. |
| Full custom splinter family | 19 full 47-focus custom splinter trees | Present, repetitive | Many have the same first-guard/stores/legitimacy/rival/doctrine/economy/League/foreign skeleton; route-specific later content varies, but early/mid play remains template-like. |
| Compact high-chaos splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `OGB` | Mixed | PRA/DSC/NRF have stronger recent high-chaos payoffs; TSC/RMC/ICD remain mechanically shallow for special actors; OGB is still only 23 focuses. |
| Factory states | `CFR_soviet_collapse_focus_tree`, `MFR_soviet_collapse_focus_tree` | Present, needs direct projects | CFR has 47 focuses and MFR 58, but many construction/arsenal focuses call one helper and no direct decision/project/building/AI surface. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` ancient trees | Present but compact | Each is 16 focuses with symbolic/expansion fork. Meets compact skeleton, but not enough depth for major high-chaos restoration play. |

## Reward Spam And Idea Churn

Direct exact duplicate reward calls inside one focus: none found.

Direct duplicate `add_ideas`, `remove_ideas`, or `swap_ideas` calls inside one focus: none found.

The main reward-spam issue is helper churn. The top focus helper calls are:

| Helper | Direct focus calls | Issue |
| --- | ---: | --- |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 138 | Very common generic depot/supply reward; many call sites do not directly build rails, hubs, trains, or supply decisions. |
| `soviet_collapse_apply_focus_military_consolidation` | 132 | Frequent military flavor without direct unit/template/war-plan payoff at many focuses. |
| `soviet_collapse_apply_focus_legal_recognition` | 117 | Common legal/political progression; risks making political branches feel same-shaped. |
| `soviet_collapse_apply_focus_republican_compact_plan` | 80 | Broad compact route helper; often substitutes for direct settlement mechanics. |
| `soviet_collapse_apply_focus_foreign_channel` | 63 | Foreign route helper; many focuses need visible target diplomacy, aid, recognition, or sponsor decisions. |
| `soviet_collapse_apply_objective_source_pressure_delta` | 63 | Pressure change helper used as payoff in routes that imply larger consequences. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 60 | Useful high-chaos identity marker, but repeated as a generic power packet. |
| `soviet_collapse_apply_focus_league_preparation` | 52 | League preparation often lacks direct League votes, member missions, joint fronts, or arbitration decisions. |

Obvious helper-transitive idea churn found:

- `soviet_collapse_update_pra_authority_idea`: 14 focus calls; helper body contains repeated `remove_ideas`/`add_ideas` lifecycle work. This is probably intended for PRA, but it is the current clearest focus-to-spirit churn hotspot.
- `soviet_collapse_add_republic_focus_recovery_progress`: 11 focus calls; helper body reaches `soviet_collapse_update_consolidated_republic_ideas`.

High-helper-count focuses that should be reviewed first:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1754`, `PRA_the_pale_line_endures`: 5 helpers, combining endgame, republican compact, rail authority, PRA idea update, and corridor network.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3110`, `DSC_claim_the_soldiers_road`: 6 helpers, including claims, cores, high-chaos identity, expansion claims, assault columns, and dead-army war launch.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3155`, `DSC_armies_that_do_not_demobilize`: 6 helpers, similar assault/claims/war stack.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3219`, `DSC_congress_of_the_dead_army`: 5 helpers plus direct war goal and AI strategy.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:442`, `FTH_war_plan`: 4 broad generic helpers and no direct keyword payoff.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2171`, `TSC_starfall_mandate`: 4 high-chaos helpers plus direct war goal and AI strategy.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2668`, `RMC_resurrection_without_state`: 4 high-chaos helpers plus assault columns.
- Ancient expansion/endgame focuses at `005_soviet_collapse_ancient_restorations.txt:229`, `:332`, `:360`, `:619`, `:718`, `:746`, `:999`, `:1107`, `:1135`, `:1389`, `:1490`: repeated expansion/high-chaos helper stack across all ancient trees.

## High-Chaos Country Audit

| Country or family | Current payoff | Gap |
| --- | --- | --- |
| `CFR` Civilian Factory of Russia | 47 focuses, construction rhetoric, one direct late war goal at `CFR_rebuild_russia_without_moscow`, some decisions/tooltips. | Many construction identity focuses have no direct reward keyword and call only one helper: `CFR_count_the_cranes` `:32`, `CFR_the_unfinished_city_speaks` `:110`, `CFR_the_board_becomes_the_cabinet` `:329`, `CFR_cities_first` `:348`, `CFR_contracts_first` `:451`, `CFR_the_city_without_citizens` `:780`, `CFR_the_concrete_republic` `:844`, `CFR_reconstruction_protectorates` `:991`. These should get major construction projects, factory-site decisions, housing pressure, concrete/engineer missions, or city expansion mechanics. |
| `MFR` Military Factory of Russia | 58 focuses, unique icons, late `MFR_eternal_arsenal_marches` war goal/AI, some factory guard and arsenal state hooks. | Many arsenal focuses call only one helper and expose no direct production/militia/armored-train surface: `MFR_arm_the_new_russia` `:2015`, `MFR_artillery_from_broken_foundries` `:2112`, `MFR_rifles_before_speeches` `:2140`, `MFR_repair_the_tank_lines` `:2159`, `MFR_armored_train_workshops` `:2590`, `MFR_state_as_one_arms_order` `:2922`, `MFR_output_is_victory` `:2943`, `MFR_no_peace_without_orders` `:2981`. |
| `PRA` Pale Railway Authority | 22 focuses, strong rail identity, corridor decisions, rail guards, a direct late war goal/AI at `PRA_rails_over_capitals`. | Still has heavy `soviet_collapse_update_pra_authority_idea` churn in 14 focuses. `PRA_the_pale_line_endures` `:1754` is helper-heavy and should collapse into one visible rail-state payoff tooltip or stronger direct route payoff. |
| `DSC` Dead Soldiers' Congress | 18 focuses, claims/cores helpers, assault columns, war goals and aggressive AI at late focuses. | Better than earlier state, but several identity focuses still have no direct unit/core/war/recruitment keyword: `DSC_witness_officers` `:2847`, `DSC_rearguard_supply_bureau` `:2981`, `DSC_letters_to_veteran_towns` `:3068`, `DSC_league_of_old_fronts` `:3090`, `DSC_republic_of_roll_calls` `:3190`. |
| `ICD` Iron Commissariat of the Dead | 18 focuses, death-state theme and one late war goal/AI. | Much weaker than DSC. Many dead-state focuses have no direct unit, core, war, or special recruitment payoff: `ICD_open_the_dead_rolls` `:3804`, `ICD_ryazan_grave_commissariat` `:3825`, `ICD_commissars_who_do_not_die` `:3928`, `ICD_funeral_guard` `:3980`, `ICD_grave_columns_march` `:4148`, `ICD_state_of_last_addresses` `:4240`. |
| `RMC` Red Martyrs | 18 focuses, theme present, one late high-chaos war route. | Route is still thin: `RMC_reliquary_guard` `:2440`, `RMC_dead_volunteer_columns` `:2491`, `RMC_claim_the_burial_roads` `:2590`, `RMC_procession_columns` `:2611`, `RMC_shrine_state` `:2706` need recruitment, cores, unit spawn, or aggressive AI hooks comparable to DSC. |
| `NRF` Northern Revenant Fleet | 18 focuses, good naval XP, port mechanics, late war goal/AI, several naval/convoy rewards. | Strongest compact naval death actor, but `NRF_claim_the_white_sea_lane` `:3654` has only high-chaos identity helper and should directly claim/target lanes or unlock port/convoy missions. |
| `KRS` Kronstadt Free Soviet | 47 focuses and many naval/port focuses. | Naval identity exists, but key skeleton focuses still generic; `KRS_endgame` `:10007` is helper-only and should have port/fleet/faction payoff. |
| `ARD` Arctic Directorate | 47-focus generic skeleton with Arctic flavor later. | Directorate/naval-port identity is still too template-like in early/mid branches: `ARD_first_guard`, `ARD_stores`, `ARD_legitimacy`, `ARD_rival`, `ARD_doctrine`, `ARD_economy`, `ARD_league`, `ARD_foreign`, `ARD_supply`, `ARD_enemy_front` around `:23026`-`:23265` mainly call generic custom-splinter helpers. |
| `NLC` Northern Lights Committee | 47 focuses, polar/ice-road industry flavor. | `NLC_war_plan` `:24556` is helper-heavy but not directly aggressive enough; `NLC_extreme_gate` `:25333` and `NLC_extreme_path` `:25401` need clearer high-chaos payoff or special mechanic. |
| `OGB` Old Great Bulgaria | 23 focuses, claims/war goal/AI at late route. | Still too shallow for required Volga restoration. Missing real depth for restoration trunk, legitimacy fork, trade/river, religion/society, future event hook, rival branch, and expansion aftermath. |
| `KZR`, `SOG`, `KHW`, `ALN` ancient restorations | Each 16 focuses, symbolic/expansion fork, direct claims/war goal in expansion route. | Meets compact skeleton but not high-chaos restoration depth. Late `*_returned_names_endgame` focuses are mostly helper stacks and need distinct diplomacy, old-border integration, League/republic interactions, or mythic failure states. |

## Missing Or Simplified Content

Highest-priority route families lacking payoff:

1. Factory state projects:
   - CFR needs more direct construction projects, housing/reconstruction pressure, factory-site decisions, and construction-city expansion.
   - MFR needs more direct arsenal quotas, production militia, armored train, proxy arming, and foreign arms-market mechanics.
2. Death-state aggression:
   - ICD and RMC need unit spawning, special recruitment, cores/claims, aggressive AI, and neighbor-war equivalents comparable to DSC.
3. OGB and ancient restoration depth:
   - OGB needs a broader Volga restoration pass.
   - KZR/SOG/KHW/ALN need more than a symbolic/expansion fork if they are expected to play as high-chaos restoration states.
4. Republic route payoffs:
   - Ukraine political endpoints, Black Sea branch, Belarus forest/rail route, Kazakhstan resource/rail/steppe branches, and Caucasus oil routes need more state-targeted and decision-linked rewards.
5. Generic custom splinter skeleton:
   - Full 47-focus splinters often vary late content but share early/mid route helper structure too closely.

## Icon Coverage Table

All focus icons are assigned and all assigned icon ids resolve to sprite definitions in repo or vanilla interface files, excluding flag paths. The issue is duplicate icon usage, not missing icons.

| Tree or family | Icon state | Risk |
| --- | --- | --- |
| Ukraine | 83 focuses, 76 unique icons, 11 repeated focus uses | `GFX_ukr_soviet_collapse_democratic` appears 4 times; political/reward identity should be diversified during route payoff work. |
| Belarus | 53 focuses, 51 unique icons, 4 repeated uses | Low risk. |
| Kazakhstan | 92 focuses, 92 unique icons | Good coverage. |
| Baltic | 42 focuses, 37 unique icons, 8 repeated uses | Reused wire/restoration/forest icons should be reviewed with route layout pass. |
| Central Asia | 45 focuses, 39 unique icons, 8 repeated uses | Reused rail/irrigation and steppe federation icons. |
| Internal republic | 62 focuses, 56 unique icons, 9 repeated uses | Shared compact identity duplication remains. |
| CFR | 47 focuses, 32 unique icons, 26 repeated uses | Highest factory icon duplication; several construction/governance icons appear 3 times. |
| MFR | 58 focuses, 58 unique icons | Good coverage. |
| IUL | 47 focuses, 24 unique icons, 38 repeated uses | Worst custom-splinter icon reuse. |
| FEV/SZA/MRC/UWD | 47 focuses each, 27-34 repeated uses | These need icon diversification alongside route-depth work. |
| Compact chaos splinters `PRA/DSC/ICD/NRF/RMC/TSC/OGB` | No missing icons, no duplicate icon uses in compact trees | Icon coverage is fine; content depth is the blocker. |
| Ancient restorations `KZR/SOG/KHW/ALN` | 16 unique icons each | Icon coverage is fine; route depth is the blocker. |

## Localisation And Reward Mismatch List

Localisation key coverage is complete. Mismatches are semantic:

- `ukr_soviet_collapse_the_directory_state` (`republics.txt:722`): title/description imply a military state, but reward lacks direct law/officer/unit/advisor/AI strategy consequence.
- `ukr_soviet_collapse_black_sea_port_ledgers` (`republics.txt:1228`): Black Sea port text needs direct naval, port, convoy, coastal, or diplomacy mechanics.
- `blr_soviet_collapse_partisans_or_army` (`republics.txt:9637`): doctrine choice text needs unit templates, spawned units, or partisan/regular mission split.
- `blr_soviet_collapse_baltic_wire_rooms` (`republics.txt:10136`): diplomacy/wire-room text needs direct Baltic/League diplomacy mechanics.
- `kaz_soviet_collapse_the_congress_chooses_a_past` (`republics.txt:10288`): major route fork text should visibly alter route locks, leaders/advisors/cosmetic identity, or state mechanics.
- `kaz_soviet_collapse_industrial_settlement_compacts` (`republics.txt:11794`): settlement/resource text needs stronger Kazakhstan resource/rail payoff.
- `PRA_the_pale_line_endures` (`custom_splinters.txt:1754`): rail-state finale is helper-heavy and should be a direct rail/supply/war/diplomacy payoff.
- `ICD_state_of_last_addresses` (`custom_splinters.txt:4240`): death-state endpoint is helper-only compared with the identity promised.
- `CFR_the_concrete_republic` (`factory_successors.txt:844`): state identity text should create stronger construction-state mechanics.
- `MFR_state_as_one_arms_order` (`factory_successors.txt:2922`): arsenal-state text should directly alter production, units, contracts, or AI.
- `OGB_the_old_name_survives_modern_war` (`factory_successors.txt:1704`): late focus has aggression hooks, but the tree lacks the preceding route depth promised by the spec.

## AI Behavior Gaps

- Every focus has `ai_will_do`, but many are local base/modifier weights rather than route-aware AI plans.
- Direct `add_ai_strategy` appears in only a minority of high-chaos final or war focuses.
- High-chaos AI is better in `PRA`, `DSC`, `NRF`, `CFR`, `MFR`, `OGB`, and ancient expansion focuses than in earlier passes, but still uneven.
- `ICD`, `RMC`, `TSC`, `ARD`, and `NLC` need stronger route-specific aggression: when to attack Moscow, when to attack neighbors, when to join/reject League structures, and when to pursue special mechanics.
- Republic AI still needs route follow-through: Ukraine political routes, Belarus forest/rail choice, Kazakhstan Alash/socialist/resource/federation choices, Caucasus oil route, Central Asian southern/old-movement route, and Moldova Romanian/Dniester choices should carry downstream AI behavior beyond focus selection.

## Layout And Pathline Risks

No same-row coordinate collisions closer than 2 x-grid units were found.

High-risk wide prerequisite lines:

- `ukr_soviet_collapse_romanian_port_route` -> `ukr_soviet_collapse_romanian_grain_and_river_bargain`, `republics.txt:1625`, dx 10, dy 1.
- `ukr_soviet_collapse_carpathian_security_belt` -> `ukr_soviet_collapse_dead_fields_living_columns`, `republics.txt:2127`, dx 10, dy 2.
- `internal_soviet_collapse_write_the_autonomy_statute` -> `internal_soviet_collapse_forest_republic_committees`, `republics.txt:3296`, dx 15, dy 2.
- `baltic_soviet_collapse_rail_to_the_ports` -> `baltic_soviet_collapse_the_legal_state_or_the_front_state`, `republics.txt:4691`, dx 13, dy 1.
- `caucasus_soviet_collapse_protect_the_oil_and_ports` -> `caucasus_soviet_collapse_oil_emergency_directorate`, `republics.txt:5648`, dx 12, dy 1.
- `caucasus_soviet_collapse_oil_emergency_directorate`/`pipeline_guard_corps` -> `caucasus_soviet_collapse_baku_oilfield_guard`, `republics.txt:5917`, dx 10-12.
- `central_asia_soviet_collapse_no_more_distant_capitals` -> `central_asia_soviet_collapse_the_southern_shield`, `republics.txt:7200`, dx 17, dy 2.
- `blr_soviet_collapse_council_bargains_with_forests` -> `blr_soviet_collapse_guide_companies`, `republics.txt:9408`, dx 23, dy 1.
- `blr_soviet_collapse_swamp_roads_closed` -> `blr_soviet_collapse_armored_train_workshops`, `republics.txt:9859`, dx 22, dy 1.
- Kazakhstan fork lines around `kaz_soviet_collapse_the_congress_chooses_a_past`, `republics.txt:10101`-`:10259`, dx 10-14.
- `kaz_soviet_collapse_the_army_that_crosses_distance` -> `kaz_soviet_collapse_steppe_federation_charter`, `republics.txt:10685`, dx 17, dy 2.
- `kaz_soviet_collapse_steppe_federation_charter` -> `kaz_soviet_collapse_the_steppe_arbitration_court`, `republics.txt:11203`, dx 17, dy 1.
- `kaz_soviet_collapse_emergency_oil_boards` -> `kaz_soviet_collapse_industrial_settlement_compacts`, `republics.txt:11588`, dx 12, dy 2.

High-risk wide mutual-exclusion spans:

- Baltic four-way fork at `republics.txt:4706`-`:4807`: `baltic_soviet_collapse_legal_continuity_government`, `military_border_government`, `baltic_league_first`, `foreign_protection_council` span dx 10-16 on one row.
- Central Asia fork at `republics.txt:6555`: `central_asia_soviet_collapse_local_republic_council` vs `central_asia_soviet_collapse_military_border_authority`, dx 8.
- Moldova fork at `republics.txt:7960`: `moldova_soviet_collapse_conditional_union` vs `moldova_soviet_collapse_reject_the_union_question`, dx 8.
- Belarus four-way route fork at `republics.txt:8943`-`:8975`: `national_council_of_minsk`, `socialist_autonomy_without_moscow`, `military_transit_directorate`, `foreign_corridor_administration` spans dx 11-18 on one row.

Do not add fake mutual exclusions to solve these. The route locks are mostly meaningful; the risk is geometry/readability, not missing exclusivity.

## High-Priority Fix Plan For Parent

1. CFR/MFR factory-state payoff tranche:
   - Add direct construction/civilian factory projects and housing/reconstruction pressure to CFR focuses listed above.
   - Add direct arsenal quota, production militia, armored train, and proxy arming mechanics to MFR focuses listed above.
   - Add route-aware AI strategy follow-through for construction expansion and arms-market aggression.
2. Death-state aggression tranche:
   - Bring `ICD` and `RMC` up to DSC standard with unit spawning, claims/cores/war goals, and AI strategy.
   - Keep helper stacks behind clean custom tooltips to avoid hover spam.
3. OGB and ancient restoration route-depth tranche:
   - Expand OGB beyond 23 focuses or explicitly document it as intentionally compact.
   - Add old-border integration, modern-republic diplomacy, League interaction, and symbolic-vs-expansionist failure states for `KZR/SOG/KHW/ALN`.
4. Republic payoff tranche:
   - Ukraine military/Black Sea/Bread route, Belarus forest/rail, Kazakhstan resource/rail/federation, Caucasus oil, Central Asian water/pass, and Moldova Dniester/Romanian route need direct mechanics tied to existing decision/effect systems.
5. Layout tranche:
   - Move only affected nodes after deciding route payoff changes, then rerun coordinate/pathline validation. Avoid meaningless new mutual exclusions.
6. Helper-spam cleanup:
   - Convert repeated broad helper stacks into route-specific wrapper helpers or direct visible payoffs where the same focus currently calls 4-6 helpers.

## Files Changed

Only this handoff was added:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_focus_reward_depth_high_chaos_audit_handoff.md`

No focus, localisation, scripted effect, decision, idea, gfx, or flag files were edited.

## Changed Focus IDs

None.

## Route Behavior Before And After

Before: current Event005 focus trees remain as parsed above.

After: no gameplay route behavior changed. This is an audit handoff only.

## Localisation Keys And Icon IDs Changed

None.

## Validation Run

Read and consulted:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: National focus modding, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs and examples: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and vanilla `common/national_focus/soviet.txt`, `generic.txt`, `baltic_shared.txt` search examples.

Static validation:

- Brace balance over the four scoped focus files: all 0.
- Unsupported `<=`/`>=` scan over the four scoped focus files: 0 hits.
- Parsed focus blocks: 1,698.
- Duplicate focus id scan: 0 duplicate ids.
- Missing `icon`: 0.
- Missing `search_filters`: 0.
- Missing `completion_reward`: 0.
- Missing `ai_will_do`: 0.
- Missing focus localisation name keys: 0.
- Missing focus localisation `_desc` keys: 0.
- Missing icon sprite definitions, scanning repo and vanilla interface `.gfx` while excluding flag paths: 0.

## Skipped Validation

- No in-game render screenshot or HOI4 launch validation was run.
- No focus-file patch validation beyond static scans was required because no focus files were edited.
- I did not inspect or edit any flag asset or flag interface path.

## Remaining Route Risks

- Current focus trees are complete at the syntax/surface level but still risk feeling shallow because many routes share generic helper progression.
- High-chaos actors are not consistently overpowered or aggressive enough, especially `ICD`, `RMC`, `TSC`, `ARD`, `NLC`, OGB, and the ancient restorations.
- CFR/MFR have enough focus count but need stronger visible construction/arsenal mechanics.
- Layout risks are mostly long prerequisite and fork spans, not hard coordinate collisions.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`

