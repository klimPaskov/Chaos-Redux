# Event 005 Soviet Collapse Focus-Tree Full Audit Handoff

Date: 2026-06-04
Role: `chaosx_focus_tree_auditor`
Scope: Read-only audit of all current Soviet Collapse focus trees.

## Read-Only Status

No gameplay files were edited in this audit pass. No tiny syntax/layout patch was made.

No files under `gfx/flags/` or `interface/flags/` were opened or edited. Flags were not touched.

## Required References Consulted

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: `National focus modding`, `Data structures`, `Triggers`, `Effect`, `Localisation`, `Modifiers`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`
- Vanilla docs:
  - `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- Vanilla precedent sampled:
  - `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
- Event 005 design/context:
  - `docs/events/005_soviet_collapse.md`
  - `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
  - `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
  - `common/scripted_effects/005_soviet_collapse_effects.txt` focus loading and successor setup sections

## Files Inspected

Primary focus files:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

Context inspected as needed:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `localisation/english/005_soviet_collapse*.yml`

## Tree Coverage

Parser count: 41 `focus_tree` blocks and 1,698 `focus = { ... }` blocks.

Ancient restorations:

- `KZR_soviet_collapse_ancient_focus_tree` - 16 focuses
- `SOG_soviet_collapse_ancient_focus_tree` - 16 focuses
- `KHW_soviet_collapse_ancient_focus_tree` - 16 focuses
- `ALN_soviet_collapse_ancient_focus_tree` - 16 focuses

Custom/high-chaos splinters:

- 47-focus full splinters: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`
- Short/crisis splinters: `PRA` 22, `TSC` 18, `RMC` 18, `DSC` 18, `NRF` 18, `ICD` 18

Factory/returned-name successors:

- `CFR_soviet_collapse_focus_tree` - 47 focuses
- `OGB_soviet_collapse_focus_tree` - 23 focuses
- `MFR_soviet_collapse_focus_tree` - 58 focuses

Republic/shared trees:

- `soviet_collapse_ukraine_focus_tree` - 83 focuses
- `soviet_collapse_breakaway_focus_tree` - 36 focuses
- `soviet_collapse_internal_republic_focus_tree` - 62 focuses
- `soviet_collapse_baltic_focus_tree` - 42 focuses
- `soviet_collapse_caucasus_focus_tree` - 40 focuses
- `soviet_collapse_central_asia_focus_tree` - 45 focuses
- `soviet_collapse_moldova_focus_tree` - 48 focuses
- `soviet_collapse_belarus_focus_tree` - 53 focuses
- `soviet_collapse_kazakhstan_focus_tree` - 92 focuses

## Executive Findings

1. Direct focus `add_ideas` spam has mostly been removed. The parser found no focus with two or more direct `add_ideas` rewards and no repeated same direct idea inside one focus.
2. Reward spam still exists through repeated helper calls, repeated flags, repeated small construction/equipment payloads, and repeated route-stage identity helpers. The worst repeated helpers are `soviet_collapse_apply_focus_depot_and_supply_control` 138 times, `soviet_collapse_apply_focus_military_consolidation` 131 times, `soviet_collapse_apply_focus_legal_recognition` 107 times, and `soviet_collapse_apply_republican_compact_plan` 80 times.
3. The largest design gap is branch depth, not raw focus count. Several trees have enough nodes but still play like repeated reward lanes instead of political, industrial, military, diplomatic, decision, and expansion systems interacting.
4. Short high-chaos successors and ancient restorations remain below the spec's "real branch" standard. They are readable skeletons, not complete playable identities.
5. Several chaos-country trees are still not aggressive enough. Many full 47-focus high-chaos trees have zero direct decision unlocks, zero direct claims, zero direct cores, and no direct war goals in the focus file, relying on generic endpoint helpers instead.
6. Layout is improved compared with older audits but not clean. There are no duplicate focus ids and no duplicate coordinates, but there are same-row `x` distance 1 pairs, two vertical pathline collisions, and many very long edges that will produce unreadable route lines.
7. Focus filters are inconsistent with rewards in many cases, especially military focuses that build forts/rail/AA without `FOCUS_FILTER_INDUSTRY`, political focuses that grant manpower, and focuses that grant war support without `FOCUS_FILTER_WAR_SUPPORT`.

## Top 25 Focus IDs Needing Rework

| Priority | Focus id | Problem | Suggested replacement reward/mechanic |
|---:|---|---|---|
| 1 | `PRA_the_board_overrules_ministers` (`custom_splinters:1369`) | One-node political route. It settles tensions and grants rails/recognition but does not become a real railway-state government path. | Add a timetable-court authority route: recurring station court decisions, rail toll income, neutral-corridor guarantees, and route-specific AI strategy to defend junctions instead of only using rail reward helpers. |
| 2 | `PRA_armored_train_directorate` (`custom_splinters:1402`) | Armored-train route is only one branch choice plus stock rail/guard rewards. | Add armored-train command mechanics: unlock armored train template/production, raiding/junction seizure decisions, rail denial missions, and stronger anti-SOV/neighbor war-plan AI when high chaos is active. |
| 3 | `TSC_tura_observation_presidium` (`custom_splinters:1838`) | Flat PP plus signal variable. This is too thin for a high-chaos anomalous authority opening. | Replace with an observatory-presidium mechanic: anomaly research variable, signal-network decisions, radar/AA state targeting, and a TSC-specific event or decision that pressures Soviet obedience/old-movement metrics. |
| 4 | `TSC_claim_the_impact_zone` (`custom_splinters:2190`) | The title promises territorial high-chaos claims but reward is only variables/helper progress. | Add explicit impact-zone claims, core-on-control handling, target decisions for neighboring Siberian states, and a mission that escalates to war if ignored. |
| 5 | `RMC_tambov_witness_cells` (`custom_splinters:2307`) | Flat PP plus martyr legitimacy; not enough for the Red Martyrs' core identity. | Unlock witness-cell decisions that convert casualties/old-movement pressure into manpower, resistance, and Soviet authority damage; add a visible route tooltip for the martyr network. |
| 6 | `RMC_claim_the_burial_roads` (`custom_splinters:2635`) | Only one state claim and generic high-chaos identity. Too small for an expansion path. | Replace with a burial-road claim package, dead-volunteer assault columns, core controlled burial-road states, and a limited neighbor-war decision gated by martyr mobilization. |
| 7 | `ICD_ryazan_grave_commissariat` (`custom_splinters:3857`) | Flat PP plus authority variable. The Iron Commissariat needs a harsher opening control system. | Unlock dead-roll audit decisions that confiscate depots, damage Soviet command obedience, and raise memorial battalions from controlled states. |
| 8 | `ICD_claim_the_unburied_front` (`custom_splinters:4191`) | One claim plus variable. Expansion is too symbolic. | Use a dead-roll front package: claims on multiple front states, core-on-control, compulsory memorial battalion deployment, and high-chaos war-plan escalation. |
| 9 | `NRF_living_harbor_committees` (`custom_splinters:3425`) | Early harbor politics still rewards as small equipment/building bundle. | Add revenant-fleet harbor mechanics: ghost convoy muster, port salvage decisions, coastal raider templates, and convoy/port disruption against SOV or nearby enemies. |
| 10 | `NRF_northern_revenant_fleet` (`custom_splinters`, focus id from NRF tree) | Endpoint exists but the tree remains 18 focuses and shallow for a naval death-state. | Make endpoint fire a northern raiding package: coastal war goals, mine/convoy AI strategy, naval infantry spawn, and port-core/occupation settlement decisions. |
| 11 | `OGB_restore_the_bolghar_name` (`factory_successors:1142`) | Flat PP/stability. This should define the restored-name state. | Add Volga legitimacy stages, cleric/scholar/notable route locks, party/cosmetic identity effects if available, and decisions to contest Kazan/Ufa legitimacy. |
| 12 | `OGB_treat_with_idel_ural` (`factory_successors:1430`) | Key compact route gives mostly PP/flag. It should decide Volga diplomacy. | Add compact mechanics: mutual guarantees or regional faction hook, Volga toll-sharing decision, defensive member call, and a clear alternative to the rival war path. |
| 13 | `KZR_old_border_files` (`ancient_restorations:177`) | Ancient restoration expansion is compressed into a reward bundle. | Add Caspian toll-claim decisions, Volga/Caspian route control mission, controlled-claim cores, and a trade/toll mechanic that competes with normal republic legitimacy. |
| 14 | `SOG_old_city_border_files` (`ancient_restorations:587`) | Same 16-focus ancient skeleton; old-city expansion lacks postwar handling. | Add Samarkand/Bukhara city-claim chain, caravan route decisions, integration/coring on controlled old cities, and merchant-polity diplomacy branch. |
| 15 | `KHW_old_oasis_border_files` (`ancient_restorations:987`) | Oasis restoration gets claims/buildings but little mechanic depth. | Add water-rights decisions, canal-control missions, oasis claim integration, and drought/supply consequences tied to KHW variables. |
| 16 | `ALN_old_pass_border_files` (`ancient_restorations:1396`) | Pass claims/buildings are a bundle, not a branch. | Add Darial/pass-control mechanics, mountain pass fortification decisions, controlled-pass cores, and a forced pass-war escalation at high chaos. |
| 17 | `CFR_construction_battalions` (`factory_successors:652`) | CFR military branch is too small and not distinct from construction rewards. | Unlock construction-battalion unit/template and worksite-security decisions; make later concrete/fort focuses consume or increase construction mandates. |
| 18 | `CFR_buy_peace_with_concrete` (`factory_successors:897`) | Diplomacy path is abstract; peace-by-concrete should be a mechanic. | Add reconstruction-protectorate contracts, targeted aid-for-nonaggression decisions, patron/dependency risk, and AI preference for buying peace when weak. |
| 19 | `MFR_every_buyer_has_a_flag` (`factory_successors:1958`) | Arms-export premise is underused and can become generic PP/flag depth. | Add arms-client decisions, dependency/client network variables, arms-for-recognition trade, and AI strategy to arm anti-Soviet neighbors. |
| 20 | `MFR_production_war_room` (`factory_successors:2250`) | Arsenal management should be central, not another production-focus reward. | Add arsenal-quota decision upgrades, emergency production missions, MIO/production-line bonuses if available, and high-chaos overproduction risk. |
| 21 | `ukr_soviet_collapse_the_ukrainian_commune_debate` (`republics:481`, x=22 y=13) | Too-close row cluster and route identity is hard to read. | Re-layout the commune debate lane and make the route unlock village commune decisions, requisition limits, and League/Black Banner consequences instead of only route flags/helpers. |
| 22 | `ukr_soviet_collapse_provincial_governors_or_elected_radas` (`republics:887`) | Very long edge from `rural_deputy_bloc` and political choice is disconnected from branch geometry. | Move under its actual political lane and give the choice governor/rada decision effects, local authority variables, and different AI weights by stability/war state. |
| 23 | `blr_soviet_collapse_join_the_league_when_war_comes` (`republics`, x=19 y=10) | Vertical pathline collision through `blr_soviet_collapse_orders_printed_like_timetables`; expansion branch is nearly absent. | Move League node out of the rail vertical, then make it unlock League freight/security-zone decisions and anti-SOV/anti-corridor contingency missions. |
| 24 | `blr_soviet_collapse_prepare_league_freight_tables` (`republics:9653`) | Long edge from `timetable_state`; rail diplomacy has mechanics but layout and branch payoff are unclear. | Split rail authority from League diplomacy: freight-table decision upgrades, shared rail reserve deployment, and regional-faction logistics payoff. |
| 25 | `moldova_soviet_collapse_republic_of_crossings` (`republics:8579`) | Worst long-edge case: distance 23 from `republic_without_a_patron`, also tied to route-fork edge. | Re-anchor under river/crossing route, split patronless republic and river-state payoffs, and add crossing-control decisions, Dniester settlement missions, and Romanian/Ukraine pressure consequences. |

## Idea-Spam and Reward-Spam Clusters

Direct visible idea spam:

- No focus currently adds two or more direct ideas.
- No repeated same direct idea within one focus was found.
- Successor setup effects still add starting ideas to special tags, which is appropriate for country setup, not focus reward spam.

Remaining repeated reward clusters:

- `soviet_collapse_apply_focus_depot_and_supply_control` - 138 uses. Useful shared helper, but overuse makes many branches feel like depot/supply variants.
- `soviet_collapse_apply_focus_military_consolidation` - 131 uses. Common across republic and splinter military paths; needs more route-specific variants.
- `soviet_collapse_apply_focus_legal_recognition` - 107 uses. Political/diplomatic branches often converge into the same recognition step.
- `soviet_collapse_apply_focus_republican_compact_plan` - 80 uses. Many state-building endpoints read similarly.
- Custom splinter skeleton helpers repeat 18-19 times each: `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `foreign`, `inner_faction`, `special_arm`, `supply`, `civil_rule`, `propaganda`, `settlement`, `industry_plan`, `hidden_doctrine`. These keep rewards consistent but make many high-chaos tags feel templated.
- Light reward focuses: parser found 38 focuses with only flag/PP/stability/war-support style rewards and no helper/building/decision/wargoal. Examples include `TSC_tura_observation_presidium`, `RMC_tambov_witness_cells`, `ICD_ryazan_grave_commissariat`, `OGB_restore_the_bolghar_name`, `OGB_scholars_guard_the_charter`, and multiple `*_birth` focuses.

## Missing Branch Families by Tree

Ancient restorations:

- `KZR`, `SOG`, `KHW`, `ALN`: each has only 16 focuses. They have labels for politics, trade/industry, guards, League, old borders, symbolic route, expansion route, and endgame, but each "branch" is usually one or two focuses. Missing real industrial branch, missing real diplomacy branch, missing postwar integration/coring decisions, missing route-specific AI beyond focus weights, and missing enough internal politics to feel like a restored ancient polity.

Short/crisis custom splinters:

- `PRA`: strongest of the short trees because it has rail decisions, but still missing a full political branch and a full expansion branch. It should become either a 35-45 focus rail-state tree or be documented as a narrow crisis tree.
- `TSC`: missing meaningful industry, military, diplomacy, and expansion depth. The anomalous observatory identity is mostly variables, radar/buildings, and an endpoint war goal.
- `RMC`: missing real industry and diplomacy. Martyr/witness politics are thin, expansion mostly arrives late and small.
- `DSC`: better connected to decisions than other short trees, but still only 18 focuses and largely one dead-army lane plus one orderly-state lane.
- `NRF`: missing full naval/economy/diplomacy split. Needs port/convoy/raider decisions and naval aggression.
- `ICD`: missing real politics/industry/diplomacy; death-roll concept remains too similar to RMC/DSC in structure.

Full 47-focus custom splinters:

- Many have full skeleton coverage, but decision/mechanic integration is uneven.
- Trees with zero direct decision unlocks in the focus file: `FTH`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`.
- Trees with zero direct claims/cores/war goals in the focus file despite chaos identity: most 47-focus custom splinters. They rely on generic endpoint helpers; this hides aggression and makes OP routes feel late and abstract.
- `UDC`, `SDZ`, `DHC`, `KHC`, `ARD`, `NLC` have especially low expansion keyword counts in the parser and need explicit aggression/settlement payoffs.

Factory/returned-name successors:

- `CFR`: has governance and strategy forks, but diplomacy and military branches remain thin. The construction mandate system is strong; the tree should route more branches into mandate spending decisions and protectorate mechanics.
- `OGB`: 23 focuses, below major high-chaos successor depth. Needs real Volga diplomacy versus rival-restoration routes, more state/city integration, and a larger identity branch.
- `MFR`: 58 focuses and stronger branch coverage, but still risks repeated production reward lanes. Arms-client diplomacy and arsenal quota mechanics need to be more central.

Republic/shared trees:

- Ukraine: broad branch coverage, but route readability and layout are still the main problem. Several political/foreign/Black Sea/Bread-state branches cross or crowd each other.
- Generic breakaway: serviceable crisis tree but expansion is weak and has no direct decision unlocks.
- Internal republic: many building rewards and broad families, but decision integration is low; no direct decision unlocks in focus file.
- Baltic: good political/military/diplomatic naming, but no direct decision unlocks and no direct war/claim tools.
- Caucasus: oil and diplomacy are present; military branch is comparatively thin and decision integration is limited.
- Central Asia: strong expansion naming but industry is shallow and some route lines are long/crossing.
- Moldova: diplomacy/foreign recognition is present, but industry/military are shallow and route geometry is poor.
- Belarus: rail and League content exist, but expansion is nearly absent and layout has pathline issues.
- Kazakhstan: largest tree; has many branches but route geography creates long lines and several branches need stronger direct decisions/claims rather than generic helpers.

## Chaos-Country OP/Aggression Gaps

High-chaos/custom splinters should feel more dangerous than ordinary republics. Current gaps:

- Many 47-focus splinters have no direct `create_wargoal`, no direct `add_state_claim`, no direct `add_state_core`, and no direct decision unlock in their focus file. The generic endpoint helpers may work, but the tree itself does not communicate aggression.
- `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, and `NLC` need at least one visible mid-tree aggression/expansion step before the endpoint.
- `TSC`, `RMC`, `ICD`, and `NRF` should receive earlier OP payoffs: forced claims, assault templates, neighbor intimidation decisions, or automatic pressure on Soviet authority/obedience/old-movement variables.
- Ancient restorations should not merely claim old borders. Their OP path should create state-specific integration, historical-route pressure, and high-chaos wars or ultimatums.

## Layout and Pathline Issues

No duplicate focus ids found.

No duplicate same-tree coordinates found.

Same-row focuses at distance `x = 1`:

- `UDC_soviet_collapse_focus_tree`: `UDC_radio_command_posts` x=2 y=9 and `UDC_signal_truck_yards` x=3 y=9.
- `CFR_soviet_collapse_focus_tree`: `CFR_german_concrete_offers` x=25 y=7 and `CFR_the_crane_as_watchtower` x=26 y=7.
- `CFR_soviet_collapse_focus_tree`: `CFR_british_reconstruction_credit` x=25 y=8 and `CFR_sappers_of_the_builder_state` x=26 y=8.
- `soviet_collapse_ukraine_focus_tree`: multiple crowded rows, including x=24/25 y=5, x=14/15 y=7, x=15/16 y=8, x=22/23/24 y=11-13, and x=26/27 y=7.
- `soviet_collapse_internal_republic_focus_tree`: x=9/10 y=5 and x=20/21 y=5.
- `soviet_collapse_central_asia_focus_tree`: x=6/7 y=6, x=8/9 y=8, x=3/4 y=4.
- `soviet_collapse_moldova_focus_tree`: x=14/15 y=7.
- `soviet_collapse_belarus_focus_tree`: x=14/15 y=5 and x=3/4 y=7.

Vertical pathline collisions:

- `soviet_collapse_moldova_focus_tree`: edge `moldova_soviet_collapse_moldova_route_fork` (12,2) to `moldova_soviet_collapse_river_guard_brigades` (12,5) runs through `moldova_soviet_collapse_ukrainian_border_compact` at y=3.
- `soviet_collapse_belarus_focus_tree`: edge `blr_soviet_collapse_state_between_armies` (19,4) to `blr_soviet_collapse_join_the_league_when_war_comes` (19,10) runs through `blr_soviet_collapse_orders_printed_like_timetables` at y=9.

Worst long-edge/pathline clutter candidates:

- `moldova_soviet_collapse_republic_without_a_patron` (3,7) to `moldova_soviet_collapse_republic_of_crossings` (21,12), distance 23.
- `UDC_diplomatic_plan` (18,4) to `UDC_loyalist_statute_guarantees` (4,10), distance 20.
- `SDZ_diplomatic_plan` (18,4) to `SDZ_chain_of_custody_statutes` (5,10), distance 19.
- `central_asia_soviet_collapse_no_more_distant_capitals` (-2,6) to `central_asia_soviet_collapse_the_southern_shield` (15,8), distance 19.
- `kaz_soviet_collapse_the_army_that_crosses_distance` (2,3) to `kaz_soviet_collapse_steppe_federation_charter` (19,5), distance 19.
- `moldova_soviet_collapse_a_small_state_between_larger_maps` (22,3) to `moldova_soviet_collapse_the_river_state` (14,13), distance 18.
- `kaz_soviet_collapse_steppe_federation_charter` (19,5) to `kaz_soviet_collapse_the_steppe_arbitration_court` (2,6), distance 18.
- `ukr_soviet_collapse_rural_deputy_bloc` (10,8) to `ukr_soviet_collapse_provincial_governors_or_elected_radas` (23,12), distance 17.
- `internal_soviet_collapse_write_the_autonomy_statute` (16,2) to `internal_soviet_collapse_forest_republic_committees` (1,4), distance 17.
- `blr_soviet_collapse_armored_train_workshops` (10,12) to `blr_soviet_collapse_the_league_depot_at_minsk` (24,15), distance 17.

Continuous focus panels:

- Parser did not find current hard overlaps between continuous focus panel top-left positions and nearby focus coordinates using a conservative panel proximity sweep.
- Still re-check screenshots after moving Ukraine, Moldova, Belarus, Kazakhstan, UDC, SDZ, and central Asia branches because long-line cleanup can easily push nodes into panel zones.

## Focus Filter Mismatch Examples

These examples are not the full list; they show recurring patterns.

- `PRA_armored_train_schools`: train tech, supply node, rail construction, and stockpile, but only `FOCUS_FILTER_ARMY_XP`; add `FOCUS_FILTER_INDUSTRY` and likely `FOCUS_FILTER_RESEARCH`.
- `TSC_perimeter_regiments`: air XP, AA, bunkers, manpower/equipment; only `FOCUS_FILTER_ARMY_XP`; add `FOCUS_FILTER_AIR_XP`, `FOCUS_FILTER_INDUSTRY`, and `FOCUS_FILTER_MANPOWER`.
- `RMC_letters_to_mourning_towns`: adds manpower but only political filter; add `FOCUS_FILTER_MANPOWER`.
- `ICD_letters_to_grieving_cities`: equipment payload but only political filter; add military/manpower or move reward into political-recognition mechanic.
- `ukr_soviet_collapse_first_republican_line`: building + manpower + war support, but lacks industry/war-support filters.
- `caucasus_soviet_collapse_oilfield_security_compacts`: manpower reward without manpower filter.
- `central_asia_soviet_collapse_dushanbe_mountain_sovereignty`: building + manpower reward without matching industry/manpower filters.
- `moldova_soviet_collapse_river_guard_brigades`: building reward without industry filter.
- `blr_soviet_collapse_orders_printed_like_timetables`: building + command/army reward without industry filter.
- `kaz_soviet_collapse_steppe_defense_council`: building reward without industry filter.

## Focus-Decision/Mechanic Disconnection

Trees with very low or zero direct focus decision unlocks need a mechanic pass:

- Zero direct focus decision unlocks: `FTH`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, generic breakaway, internal republic, Baltic, Moldova.
- One direct unlock: `TSC`, `RMC`, `ICD`, `NLC`.
- Two direct unlocks: `BSC`, `TNC`, `ALA`.

This does not mean no helper or decisions exist elsewhere, but the focus trees do not visibly evolve decision categories enough. Add or expose decision unlocks for:

- high-chaos expansion and neighbor pressure
- rail/port/river/oasis/pass control
- League logistics and security mandates
- foreign recognition and patron risk
- postwar integration/coring
- route-specific military deployment

## Recommended Implementation Order

1. Fix hard layout first: the two vertical pathline collisions, all same-row x=1 pairs, and the worst Ukraine/Moldova/Belarus/Kazakhstan long edges.
2. Deepen short high-chaos trees before polishing full trees: `TSC`, `RMC`, `NRF`, `ICD`, then decide whether `PRA` and `DSC` stay short or grow to full successor depth.
3. Expand ancient restorations as a batch: add shared old-name restoration mechanics, then per-tag old-route/payoff decisions for `KZR`, `SOG`, `KHW`, and `ALN`.
4. Add visible aggression to 47-focus high-chaos splinters: at least one mid-tree claim/war/ultimatum/raider decision and one postwar settlement hook before endpoint.
5. Rework `OGB` to full returned-name successor depth or explicitly classify it as a narrow crisis tree in docs.
6. Clean reward helper repetition: keep shared helpers, but add route-specific wrappers or direct decision unlocks so political, military, industry, diplomacy, and expansion paths do not all feel like depot/recognition variants.
7. Run a filter pass after reward rewrites, not before, because reward changes will alter correct filters.
8. Update docs and any count-bearing surfaces after focus counts change.

## Validation Run

Read-only checks run during this audit:

- `rg --files common/national_focus | rg '005_soviet_collapse'`
- Structured parser over all four `005_soviet_collapse*.txt` focus files:
  - 41 focus trees
  - 1,698 focus blocks
  - 0 missing `ai_will_do`
  - 0 duplicate focus ids
  - 0 duplicate same-tree coordinates
  - same-row x=1 pairs listed above
  - 2 vertical pathline collisions listed above
- Reward/effect parser over focus blocks:
  - no direct multi-idea focus reward found
  - no repeated same direct idea in one focus found
  - repeated helper clusters listed above
- Focus loading context checked in `common/scripted_effects/005_soviet_collapse_effects.txt`.

No gameplay validation was run. This was a static audit handoff only.

No files under `gfx/flags/` or `interface/flags/` were touched.
