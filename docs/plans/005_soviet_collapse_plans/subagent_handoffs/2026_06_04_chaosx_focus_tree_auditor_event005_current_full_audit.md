# Event005 Soviet Collapse Focus Tree Audit Handoff

Subagent: `chaosx_focus_tree_auditor`
Date: 2026-06-04
Scope: current Event005 Soviet Collapse focus trees only. No gfx, flags, interface, or sprite files touched.

## References Used

- Repo skill: `.agents/skills/hoi4-focus-trees/SKILL.md`
- Repo skill: `.agents/skills/hoi4-decisions-missions/SKILL.md` for focus-to-decision integration checks
- Offline wiki snapshot pages opened: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla references opened: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `common/national_focus/soviet.txt`

## Files Inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/005_soviet_collapse_ukraine_bread_state_decisions.txt`
- `common/decisions/005_soviet_collapse_kazakhstan_route_decisions.txt`
- `common/decisions/005_soviet_collapse_moldova_route_decisions.txt`
- `common/decisions/005_soviet_collapse_central_asia_league_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `localisation/english/005_soviet_collapse*.yml`

## Current Tree Inventory

Mechanical parse found 41 focus trees and 1,698 focus blocks:

- Republics file: Ukraine 83, generic breakaway 36, internal republic 62, Baltic 42, Caucasus 40, Central Asia 45, Moldova 48, Belarus 53, Kazakhstan 92.
- Custom splinters: FTH 47, PRA 22, TSC 18, RMC 18, DSC 18, NRF 18, ICD 18, and 21 other custom/splinter trees at 47 focuses each.
- Factory/ancient files: CFR 47, OGB 23, MFR 58, KZR/SOG/KHW/ALN 16 each.

Every parsed focus has an `ai_will_do` block. The remaining AI problem is route specificity and aggression gating, not missing blocks.

## High-Priority Findings

### 1. Ukraine Layout Still Has Major Crossing and Route-Lock Problems

The Ukraine tree remains the worst layout hotspot. Mechanical line checks plus manual review found route-lock and branch edges crossing heavily around the statehood fork and early political lanes:

- `ukr_soviet_collapse_question_of_statehood` at `common/national_focus/005_soviet_collapse_republics.txt:145` draws a long dependency line to `ukr_soviet_collapse_german_liaison_question` at line 1349 that passes through `ukr_soviet_collapse_black_banner_compact` at line 268.
- The opening trunk has crossed edges: `ukr_soviet_collapse_guard_the_telegraph_house` line 54 to `ukr_soviet_collapse_question_of_statehood` line 145 crosses `ukr_soviet_collapse_seal_the_grain_ledgers` line 81 to `ukr_soviet_collapse_village_granary_guards` line 1163 and to `ukr_soviet_collapse_dnieper_workshops` line 1183.
- Socialist/democratic lanes cross repeatedly: `ukr_soviet_collapse_socialist_republic_without_moscow` line 234 to `ukr_soviet_collapse_peasant_socialist_congress` line 336 and `ukr_soviet_collapse_workers_congress_in_kharkiv` line 354 cross `ukr_soviet_collapse_elections_under_shellfire` line 308 to `ukr_soviet_collapse_free_soil_compromise` line 776 / `ukr_soviet_collapse_coalition_of_three_ministries` line 808.
- `ukr_soviet_collapse_workers_congress_in_kharkiv` line 354 to `ukr_soviet_collapse_purge_moscow_loyalists` line 398 crosses `ukr_soviet_collapse_re_register_the_party` line 428 to `ukr_soviet_collapse_the_ukrainian_commune_debate` line 484 and `ukr_soviet_collapse_rural_deputy_bloc` line 829 to `ukr_soviet_collapse_provincial_governors_or_elected_radas` line 890.
- The first route locks use hidden `available` exclusions instead of visible `mutually_exclusive` links: socialist line 234, black banner line 268, democratic line 308, officer/other route locks later. This hides exclusivity from the player and makes the layout less legible.

Recommended fix: make the four early Ukraine route choices a clear horizontal or vertical mutex row under `ukr_soviet_collapse_question_of_statehood`, then move late diplomacy/foreign aid nodes out of that pathline. Do this before further reward work because reward lines are hard to audit while the layout is tangled.

### 2. Belarus Rail/League Branch Has Confirmed Pathline and Mutex Crossings

Belarus is improved relative to Ukraine but still has visible rail/league layout faults:

- `blr_soviet_collapse_timetable_state` line 9199 to `blr_soviet_collapse_league_supply_timetables` line 9222 crosses/sits through `blr_soviet_collapse_red_without_the_center` line 9007.
- `blr_soviet_collapse_quiet_recognition_letters` line 9622 to `blr_soviet_collapse_prepare_league_freight_tables` line 9644 crosses/sits through `blr_soviet_collapse_join_the_league_when_war_comes` line 9673.
- `blr_soviet_collapse_national_council_of_minsk` line 8869 to `blr_soviet_collapse_join_the_league_when_war_comes` line 9673 crosses/sits through `blr_soviet_collapse_red_without_the_center` line 9007.
- The mutex between `blr_soviet_collapse_railway_neutrality` line 9296 and `blr_soviet_collapse_rail_war_state` line 9317 crosses dependency edges from `blr_soviet_collapse_timetable_state` line 9199 to `blr_soviet_collapse_prepare_league_freight_tables` line 9644 and from `blr_soviet_collapse_league_supply_timetables` line 9222 to `blr_soviet_collapse_armored_train_workshops` line 9837.

Recommended fix: split Belarus rail into one clean lane and move league freight/recognition above or below the rail-war mutex row. Keep `railway_neutrality` and `rail_war_state` adjacent with no focus-line edge passing between them.

### 3. High-Chaos Expansion Payoffs Are Still Very Aggressive

Chaos successor endgame helpers can rapidly over-escalate by giving assault units, wargoals, AI conquer/antagonize strategies, and sometimes direct declarations:

- `soviet_collapse_spawn_custom_splinter_assault_columns_payload` in `common/scripted_effects/005_soviet_collapse_effects.txt:7882` grants manpower/equipment and creates dynamic assault/raider units.
- `soviet_collapse_apply_custom_splinter_expansion_claims_payload` at line 7953 cores every controlled non-core state, creates a SOV wargoal, creates neighbor wargoals, adds conquer/antagonize AI strategies, and can directly declare war at lines 7976 and 8002 when hidden-doctrine or high chaos gates are met.
- `soviet_collapse_apply_high_chaos_neighbor_expansion_plan` at line 9305 adds claims on neighbors and can directly declare war on breakaway neighbors at line 9342 or line 9402.
- These effects are called from many final focuses/endgame effects, including `soviet_collapse_complete_pale_railway_endgame` line 16606, `soviet_collapse_complete_tunguska_star_endgame` line 16639, `soviet_collapse_complete_iron_commissariat_endgame` line 16673, `soviet_collapse_complete_dead_soldiers_endgame` line 16716, and many 47-focus custom splinter endgames.

This may fit death-state/high-chaos identities such as DSC/NRF/ICD/RMC, but it is too broad when applied to more political, regional, or defensive identities. It also risks AI snowballing because the wargoal and AI strategy package is shared.

Recommended fix: split the shared expansion helper into identity tiers:

- death-state / terminal-chaos: direct declarations allowed only at chaos tier 5 or explicit terminal flags
- militant but territorial: claims and wargoals, no instant declarations
- defensive/republican/restoration: claims plus settlement/integration decisions, not blanket neighbor war plans

### 4. Focus Rewards Still Have Many Flat/Generic Nodes

There is no direct `add_ideas =` in the focus files. Idea application is mainly via scripted effects, and the obvious repeated-idea helper `soviet_collapse_update_pra_authority_idea` at `common/scripted_effects/005_soviet_collapse_effects.txt:7630` clears prior PRA authority ideas before adding a replacement, so it is not currently an idea-stack bug.

The bigger reward issue is flat reward density. Mechanical scan found weak flat reward candidates with no decision hook, no claims/cores/wargoals, no unit/tech/building unlock, and no strong bespoke helper. Highest counts:

- Kazakhstan: 15 weak-flat candidates, including `kaz_soviet_collapse_alma_ata_emergency_congress` line 10004, `kaz_soviet_collapse_the_alash_courts` line 10232, `kaz_soviet_collapse_lone_steppe_state` line 10719.
- Ukraine: 13, including `ukr_soviet_collapse_emergency_rada` line 37, `ukr_soviet_collapse_question_of_statehood` line 145, `ukr_soviet_collapse_elections_under_shellfire` line 308, `ukr_soviet_collapse_peasant_socialist_congress` line 336.
- OGB: 8, including `OGB_restore_the_bolghar_name` line 1129, `OGB_scholars_guard_the_charter` line 1172, `OGB_clerics_guard_the_charter` line 1192, `OGB_society_of_the_restored_name` line 1334.
- Moldova: 6, including `moldova_soviet_collapse_chisinau_emergency_council` line 7571 and `moldova_soviet_collapse_constitutional_sfat` line 8109.
- Belarus: 6, including `blr_soviet_collapse_minsk_emergency_office` line 8717, `blr_soviet_collapse_council_bargains_with_forests` line 8987, `blr_soviet_collapse_village_warning_bells` line 9409.

These focuses can remain simple only if nearby focuses carry the mechanic. Right now many are still "small stability/manpower/PP plus flag" and do not visibly change decisions, route access, AI behavior, leader/country identity, map state, or economy.

### 5. Several Trees Have Insufficient Decision Integration

Decision integration is uneven:

- Stronger integration: PRA has 14 decision hooks and a good decision surface (`pra_consolidate_timetable_courts` line 7211, `pra_mobilize_station_guard` line 7240, `pra_repair_the_branch_lines` line 7278, `pra_drive_the_junction_columns` line 7364, `pra_declare_the_moving_state` line 7413). Ukraine also has real bread-state and league decision files.
- Weak/no hooks: generic breakaway tree has 0 decision hooks, internal republic tree 0, Baltic 0, Moldova 0 in the focus file despite a separate Moldova route decision file existing, and most 47-focus custom splinter trees have 0.
- Belarus has only 3 focus-level decision hooks despite its rail/corridor identity.

Recommended fix: add route-specific decision surfaces to the large republic trees before polishing minor reward numbers. Start with Belarus rail/corridor, Moldova river/crossing/union-route decisions, and Kazakhstan steppe/southern shield/resource-town decisions.

### 6. Expansion and Claim Focuses Without Postwar/Decision Handling

Specific expansion/recovery focuses add claims or war goals but do not unlock settlement/integration decisions at the focus site:

- `central_asia_soviet_collapse_khwarazm_restoration_debate` at `common/national_focus/005_soviet_collapse_republics.txt:7380` adds 7 claims with no decision hook in the focus.
- Ancient restoration expansion focuses add claims/wargoals and shared high-chaos expansion helpers without local settlement handling: `KZR_expansionist_steppe_levy` line 236, `KZR_road_beyond_the_caspian` line 370, `SOG_expansionist_merchant_claims` line 629, `SOG_cities_beyond_the_desert` line 759, `KHW_expansionist_water_claims` line 1012, `KHW_delta_without_a_center` line 1152, `ALN_expansionist_mountain_claims` line 1406, `ALN_every_pass_a_border` line 1540.
- OGB and MFR have more bespoke payoff structure, but OGB still uses strong war/endgame helpers at `common/national_focus/005_soviet_collapse_factory_successors.txt:1630` and `common/scripted_effects/005_soviet_collapse_effects.txt:16460`.

Recommended fix: each expansion focus should either unlock target/integration decisions or call a scoped postwar settlement helper. War goals alone should not be the payoff.

### 7. Small Special Trees Still Lack Full Branch Families

The 16-18 focus trees are functional but not "full" country trees under the focus-tree skill standard:

- KZR/SOG/KHW/ALN: 16 focuses each. They have identity, claims, and endgame, but political/industry/expansion/military/diplomacy are compressed into short ladders with limited route choice.
- TSC/RMC/ICD: 18 focuses each and only 1 decision hook each. Their high-chaos concepts are strong, but most branch families are shallow.
- DSC/NRF are better connected by decisions than TSC/RMC/ICD but still rely heavily on shared endgame aggression.
- OGB has 23 focuses but 8 weak-flat candidates and should be expanded or treated as a special short tree with explicit limited-scope acceptance.

Recommended fix: either document them as intentionally compact special trees or deepen them to at least one meaningful political fork, one industry/logistics branch, one expansion/settlement branch, and one identity-specific mechanic branch.

## Top Implementation Order

1. Ukraine layout pass: rebuild the statehood route-lock row and move foreign/diplomacy/industry branches so pathlines stop crossing. Add visible mutex where route identity is exclusive.
2. Belarus layout pass: isolate the rail-war mutex and league freight lane; remove pathlines through `red_without_the_center` and `join_the_league_when_war_comes`.
3. Split high-chaos expansion helpers into identity/aggression tiers and update endgame callers.
4. Add decision surfaces to Belarus, Moldova, Kazakhstan, generic breakaway/internal republic, and selected 47-focus custom splinter trees.
5. Replace flat reward nodes in Kazakhstan, Ukraine, OGB, Moldova, and Belarus with mechanic links, decision unlocks, scoped map rewards, or route state changes.
6. Add postwar/settlement handling to claim/wargoal focuses, especially Central Asia and ancient restorations.
7. Decide whether 16-18 focus special trees are accepted compact trees or need full branch expansion.

## Validation Performed

- Parsed all four Event005 focus files for focus tree count, focus count, `ai_will_do`, prerequisites, mutexes, coordinates, decision hooks, wargoal/claim/core effects, direct idea application, and shallow reward candidates.
- Parsed `common/scripted_effects/005_soviet_collapse_effects.txt` for `add_ideas` / `swap_ideas` helpers and mapped focus callers where direct.
- Ran geometric checks for prerequisite-edge crossings, mutex-edge crossings, and focuses sitting on pathlines.

No gameplay files were patched. No simplifications or fallbacks were used.
