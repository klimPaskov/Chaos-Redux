# Event 005 Soviet Collapse Focus Tree Quality Audit

Date: 2026-06-05
Mode: read-only audit; no gameplay, gfx, or flag files edited.

## Scope

Audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` only for reward/helper interpretation.

Required references consulted before opening target files:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla focus precedents: `common/national_focus/estonia.txt`, `common/national_focus/germany.txt`

Skill used: `hoi4-focus-trees`.

## Validation Method

Parsed all `focus_tree` and top-level `focus` blocks in the four target files, extracted focus IDs, line numbers, coordinates, prerequisites, mutual exclusions, and completion rewards, then cross-checked helper calls in `005_soviet_collapse_effects.txt`.

Counts:

- 41 focus trees, 1,698 focus blocks.
- No direct `add_ideas`, `swap_ideas`, or `add_timed_idea` in the four focus files.
- Direct reward signals in the four focus files: 242 focuses add stability, 125 add political power, 109 add manpower, 139 add equipment stockpiles, 336 add building construction, 13 add direct claims, 13 create war goals, 22 add AI strategies.
- 1,657 prerequisite focuses do not use `relative_position_id`; the wiki says relative positioning is preferred for prerequisite branches and parents should sit above children for reliable path sprites.

## Top Layout And Pathline Issues

These are the highest-impact visible pathline problems by parent-child horizontal span, multi-parent spread, or awkward join geometry.

- `moldova_soviet_collapse_republic_of_crossings` at `(21,12)`, line 8715, has extreme incoming lines from `moldova_soviet_collapse_republic_without_a_patron` `(3,7)`, `dx=18`, and `moldova_soviet_collapse_moldova_route_fork` `(12,2)`, `dy=10`. This is a late join pulled far right and down from separate branches.
- `central_asia_soviet_collapse_the_southern_shield` at `(15,9)`, line 7293, pulls from `central_asia_soviet_collapse_no_more_distant_capitals` `(-2,6)`, `dx=17`, and `central_asia_soviet_collapse_desert_scout_columns` `(7,6)`, `dx=8`. This likely creates a long diagonal/zig-zag across the tree.
- `ukr_soviet_collapse_grain_census_of_everyone` at `(31,18)`, line 2152, pulls from `ukr_soviet_collapse_appointed_governors` `(15,14)`, `dx=16`. The bread-state path is visually far from its parent chain.
- `blr_soviet_collapse_league_supply_timetables` at `(0,12)`, line 9353, pulls from `blr_soviet_collapse_timetable_state` `(16,8)`, `dx=-16`. This is a hard left jump.
- `kaz_soviet_collapse_steppe_federation_charter` at `(18,6)`, line 10797, pulls from `kaz_soviet_collapse_the_army_that_crosses_distance` `(2,3)`, `dx=16`. The federation branch is connected across unrelated space.
- `ukr_soviet_collapse_foreign_courts_notice_kyiv` at `(29,4)`, line 731, pulls from `ukr_soviet_collapse_question_of_statehood` `(13,3)`, `dx=16`, `dy=1`. One-row connections this wide are especially ugly.
- `kaz_soviet_collapse_the_steppe_arbitration_court` at `(2,7)`, line 11320, pulls from `kaz_soviet_collapse_steppe_federation_charter` `(18,6)`, `dx=-16`, `dy=1`.
- `blr_soviet_collapse_baltic_wire_rooms` at `(31,12)`, line 10067, pulls from `blr_soviet_collapse_state_between_armies` `(16,7)`, `dx=15`.
- `internal_soviet_collapse_forest_republic_committees` at `(1,4)`, line 3320, pulls from `internal_soviet_collapse_write_the_autonomy_statute` `(16,2)`, `dx=-15`.
- `BAC_militia_training_yards` at `(15,9)`, line 22664, pulls from `BAC_war_plan` `(0,8)`, `dx=15`, `dy=1`.
- `UDC_loyalist_statute_guarantees` at `(4,10)`, line 10865, pulls from `UDC_diplomatic_plan` `(18,4)`, `dx=-14`.
- `SDZ_chain_of_custody_statutes` at `(5,10)`, line 12094, pulls from `SDZ_diplomatic_plan` `(18,4)`, `dx=-13`.

Repeated multi-parent join issues:

- `FEV_endgame` `(10,13)`, line 17275, has parent spread 16 across `FEV_extreme_path` `(3,12)`, `FEV_settlement` `(6,7)`, `FEV_authority_from_the_harbor` `(12,12)`, `FEV_amur_buffer_posts` `(0,10)`, `FEV_pacific_between_empires` `(16,12)`, and others.
- `SZA_endgame` `(10,15)`, line 18444, has parent spread 14 across `SZA_extreme_path` `(3,12)`, `SZA_settlement` `(6,7)`, `SZA_baikal_rear_area` `(2,10)`, `SZA_siberia_between_oceans` `(16,12)`, and others.
- `BAC_endgame` `(8,18)`, line 23083, has parent spread 14 across `BAC_extreme_path` `(3,11)`, `BAC_obluchye_rear_area` `(0,13)`, `BAC_league_relief_bargain` `(14,12)`, and others.
- `ARD_endgame` `(8,18)`, line 24281, has parent spread 12 across `ARD_extreme_path` `(5,13)`, `ARD_kandalaksha_rear_area` `(0,13)`, `ARD_league_convoy_bargain` `(12,12)`, and others.
- Ancient trees have clean small grids but repeated wide center joins: `KZR_league_transit_bargain` `(6,4)` joins parents at `(0,3)` and `(12,3)`; `KHW_league_irrigation_bargain` and `ALN_league_pass_bargain` repeat the same 12-wide join.

## Direct Ideas And Repeated Reward Findings

Direct focus-file ideas:

- No direct `add_ideas`, `swap_ideas`, or `add_timed_idea` were found in the four target focus files.

Helper-mediated idea changes:

- `DSC_revenant_staff_line`, line 2992, calls `soviet_collapse_apply_dsc_revenant_staff_line_focus`, which calls `soviet_collapse_update_dsc_dead_army_idea`; that helper removes `dsc_grave_regiment_rivalries`/`dsc_dead_soldiers_congress` and adds `dsc_dead_army_politics`.
- Setup helpers in `005_soviet_collapse_effects.txt` add one starting identity idea per high-chaos successor on release, such as `cfr_construction_mandates`, `mfr_arsenal_quotas`, `fth_free_territory_communes`, `bsc_oasis_confederation`, `dsc_dead_soldiers_congress`, `nrf_northern_revenant_fleet`, `nlc_polar_survival_commune`. These are release setup effects, not direct focus rewards.

Repeated reward/helper packets:

- `soviet_collapse_apply_focus_depot_and_supply_control` is used by 142 focuses. Examples: `ukr_soviet_collapse_seal_the_grain_ledgers`, `ukr_soviet_collapse_depot_motor_columns`, `soviet_collapse_secure_ministry_ledgers`, `soviet_collapse_stabilize_food_and_currency`.
- `soviet_collapse_apply_focus_military_consolidation` is used by 131 focuses. Examples: `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_army_supremacy`, `soviet_collapse_factory_defense_committees`, `soviet_collapse_military_defense_council`.
- `soviet_collapse_apply_focus_legal_recognition` is used by 108 focuses. Examples: `ukr_soviet_collapse_guard_the_telegraph_house`, `ukr_soviet_collapse_republic_of_laws`, `soviet_collapse_guard_the_radio_stations`, `internal_soviet_collapse_convene_republic_presidium`.
- `soviet_collapse_apply_focus_republican_compact_plan` is used by 95 focuses.
- `soviet_collapse_apply_focus_foreign_channel` is used by 66 focuses.
- Custom splinter identity helpers are repeated in 14-tree batches: `*_first_guard_identity`, `*_stores_identity`, `*_legitimacy_identity`, `*_rival_identity`, `*_special_arm_identity`, `*_supply_identity`, `*_civil_rule_identity`, `*_propaganda_identity`, `*_settlement_identity`, `*_industry_plan_identity`.

Finding: the user complaint about "idea-like/spammy rewards" is valid in effect even though direct `add_ideas` spam is gone. Many focuses still resolve to shared stat/variable packets, small construction/equipment/stability grants, or identity helper calls repeated across many countries. The next pass should not simply remove helpers; it should replace repeated helper-only nodes with route-specific unlocks, decisions, war plans, map changes, advisors, special units, or unique mechanic thresholds.

## Shallow Branch And Tree Findings

- The 18-focus special trees remain too short for playable chaos countries: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`. They have flavor identity but not enough political/industry/diplomacy/expansion branch mass to feel like full countries.
- The 16-focus ancient trees (`KZR`, `SOG`, `KHW`, `ALN`) are structurally readable but are mostly the same pattern: council/law/registers, market/workshop, guard/patrol, old border files, symbolic vs expansion fork, charter, two end nodes. They need at least one unique mechanic branch each, not just claims plus a symbolic/expansion pair.
- The 47-focus custom splinter trees have better size, but many share the same skeleton: `birth`, `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `diplomatic_plan`, `inner_faction`, `special_arm`, `supply`, `enemy_front`, `war_plan`, `civil_rule`, `propaganda`, `settlement`, `radical_turn`, `industry_plan`, `hidden_doctrine`, `extreme_gate`, `endgame`, `extreme_path`. This makes the branch labels clearer than before but still template-driven.
- Political/industry/expansion branches are visually and mechanically blurred in several republic trees because long parent jumps connect political decisions to far-away industry/expansion payoffs. Moldova, Belarus, Kazakhstan, Central Asia, and Ukraine have the worst examples listed above.
- `CFR_soviet_collapse_focus_tree` is thematically coherent but still reads as repeated construction-state branches. The path around `CFR_apartment_blocks_for_loyalty` `(11,10)`, `CFR_cities_first` `(11,9)`, and `CFR_rails_first` creates odd joins and reward repetition around housing/public works.
- `MFR_soviet_collapse_focus_tree` is the strongest of the factory successors for aggression/reward identity, but it still repeats arsenal quota/security/output helpers enough that the late branch risks feeling like escalating modifiers rather than a war-economy mechanic.

## Chaos OP And Aggression Gaps

Hard aggression is concentrated in a few trees:

- War goals are present in only 13 focus blocks across all four target files.
- AI strategy additions are present in only 22 focus blocks across all four target files.
- Direct claim effects are present in only 13 focus blocks, with more claims hidden behind helper payloads.

Trees with strong aggression signals:

- `MFR_soviet_collapse_focus_tree`: `MFR_no_peace_without_orders`, `MFR_eternal_arsenal_marches`, and several AI strategy focuses make it the closest to OP/aggressive.
- `DSC_soviet_collapse_focus_tree`: `DSC_congress_of_the_dead_army` and `DSC_revenant_staff_line` have war pressure, AI strategy, assault columns, and the only helper-mediated focus idea upgrade.
- Ancient expansion nodes (`KZR_expansionist_steppe_levy`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, `ALN_expansionist_mountain_claims`) add claims/wargoals/AI, but the rest of each ancient tree is compact and not especially overpowered.

Trees/gaps that still look under-aggressive for chaos successors:

- `BSC`, `UDC`, `SDZ`, and `NLC` have assault-column/claim helper paths but little direct AI strategy pressure; they need more explicit conquer/antagonize behavior and staged neighbor war goals.
- `TNC`, `ALA`, `BBH`, `KRS`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `ARD` mostly have one `extreme_path` or local high-chaos identity endpoint, not enough repeated aggressive pressure across the route.
- `PRA`, `TSC`, `RMC`, `ICD`, `NRF`, and `OGB` have compact aggression endpoints, but most of their tree is still setup/identity rather than a snowballing threat.

## Prioritized Patch Recommendations

1. Fix pathline geometry before more reward work.
   Move or split the worst long joins listed above. Use `relative_position_id` on branch chains after the cleanup so future coordinate edits move whole branches together. Start with Moldova, Central Asia, Ukraine bread-state, Belarus timetable/league, Kazakhstan federation/arbitration, UDC/SDZ guarantee joins, and BAC/FEV/SZA/ARD endgame joins.

2. Split repeated multi-parent endgame joins into visible branch gates.
   For FEV/SZA/BAC/ARD and similar trees, add intermediate "route consolidation" gates close to their parent clusters, then feed the final endgame from 2-3 nearby gates instead of 6-9 parents spread across the tree.

3. Replace repeated helper-only custom splinter trunk nodes.
   The 14-tree custom splinter skeleton should keep shared helpers only for shared infrastructure. Each tree needs 3-5 bespoke branch-defining focuses that unlock unique decisions, war plans, state targets, unit templates, advisors, or route-specific laws instead of only `*_identity` helpers.

4. Make chaos aggression route-wide, not endpoint-only.
   Add staged aggression to weak chaos trees: early raid/claim pressure, midgame neighbor war preparation, late wargoal or scripted war launch, and AI conquer/antagonize strategies. Route this through existing high-chaos helper patterns where possible, but make the focus IDs and target sets country-specific.

5. Consolidate generic reward packets behind branch mechanics.
   For the most repeated helpers (`depot_and_supply_control`, `military_consolidation`, `legal_recognition`, `republican_compact_plan`), stop using them as the main payoff. Use them as supporting effects attached to focuses that primarily unlock decisions, missions, state construction targets, claims, advisors, faction mechanics, or visible special values.

6. Deepen the short special/ancient trees.
   Bring 16-18 focus trees up with distinct political/internal, industry/logistics, expansion, and endgame branches. Ancient trees especially need unique restoration mechanics per identity, not the same restoration grid with renamed market/pass/water terms.

7. Add branch labels through structure, not comments.
   The complaint about unclear political/industry/expansion branches is mostly a layout and reward problem. Keep politics near the political route split, industry/logistics in a coherent central or side column, and expansion on a distinct outer branch with claims/wars/settlement decisions.

## Completion Notes

No source files, gfx files, or flag assets were edited. This handoff is the only file created.
