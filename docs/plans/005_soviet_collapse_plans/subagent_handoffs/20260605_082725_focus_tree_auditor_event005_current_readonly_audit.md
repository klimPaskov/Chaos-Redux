# Event 005 Soviet Collapse Focus Tree Audit Handoff

Timestamp: 2026-06-05 08:27:25 UTC

Subagent role: `chaosx_focus_tree_auditor`

Scope: read-only audit of:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No gameplay files, localisation files, or flag assets were edited. I did not touch `gfx/flags` or any flag sprite files.

## References Consulted

Required offline wiki pages consulted before drawing conclusions:

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

Vanilla docs and precedents consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- Representative vanilla focus files: `estonia.txt`, `germany.txt`, `finland.txt`

Key reference conclusions used in this audit:

- Focus prerequisites inside one `prerequisite = { focus = a focus = b }` block are OR; separate prerequisite blocks are AND.
- Focus tree `country = { ... }` selection is not continuously refreshed; runtime trees need explicit loading.
- Focus `available = { ... }` gates do not create graph lines and can hide route locks from the player.
- `ai_will_do` is MTTH-style weighting and should be route/context-aware for major branches.

## Quantified Reward Spam Analysis

Parsed scope:

- 41 focus trees.
- 1,698 focus blocks.
- Brace balance: all four audited files ended at balance 0 with no negative depth.

Direct idea spam:

- Direct `add_ideas`: 0 occurrences.
- Focuses with duplicate direct ideas in one completion reward: 0.
- `rg -n "add_ideas"` over the four audited focus files returned no matches.

Direct small equipment/building clutter:

- Direct `add_equipment_to_stockpile`: 140 operations in 139 focuses.
- Tiny/small equipment operations: 71 operations in 70 focuses.
- Direct `add_building_construction`: 412 operations in 336 focuses.
- Level-1 direct building operations: 404 operations in 336 focuses.

Examples of small equipment rewards that should be folded into stronger systems or route-specific packages:

- `ukr_soviet_collapse_count_the_depot_keys`: 60 support equipment.
- `PRA_armored_train_schools`, `PRA_claim_the_branch_lines`, `PRA_seize_the_junction_cities`: repeated train rewards.
- `NRF_living_harbor_committees`: small infantry equipment plus 2 convoys.
- `DHC_convoy_autonomy_guarantees`, `DHC_river_port_tolls`, `DHC_league_passage_bargain`: repeated 2-convoy rewards.
- `NLC_ice_road_customs`: train reward plus one rail/infrastructure/supply package.

Examples of direct level-1 building clutter:

- `ukr_soviet_collapse_arsenal_cities`: one arms factory plus one civilian factory.
- `ukr_soviet_collapse_black_sea_port_ledgers`: one naval base plus one dockyard.
- `internal_soviet_collapse_*`: many one-state infrastructure/factory additions.
- `MFR_*`: repeated one arms factory additions across arsenal focuses.
- `NLC_*`: repeated one radar/infrastructure/supply node additions.

Repeated helper-only focus rewards:

- 625 focuses complete primarily through helper effects without direct visible map, war, decision, unit, or diplomatic payload in the focus file.
- By file: republics 147, custom splinters 386, factory successors 60, ancient restorations 32.
- Highest tree counts: `MFR_soviet_collapse_focus_tree` 31, `CFR_soviet_collapse_focus_tree` 25, `DHC_soviet_collapse_focus_tree` 23, `BAC_soviet_collapse_focus_tree` 23, `soviet_collapse_baltic_focus_tree` 22, `SDZ_soviet_collapse_focus_tree` 22, `GAC_soviet_collapse_focus_tree` 22, `FEV_soviet_collapse_focus_tree` 22, `SZA_soviet_collapse_focus_tree` 22, `IUL_soviet_collapse_focus_tree` 22.
- Most repeated helpers: `soviet_collapse_apply_focus_depot_and_supply_control` 142, `soviet_collapse_apply_focus_military_consolidation` 132, `soviet_collapse_apply_focus_legal_recognition` 108, `soviet_collapse_apply_focus_republican_compact_plan` 95, `soviet_collapse_apply_focus_foreign_channel` 66, `soviet_collapse_apply_focus_security_supply_plan` 64.

This is better than raw idea spam, but it still risks focus sameness. The parent should keep the shared helpers, but major and high-chaos trees need visible payoff layers on top of them: unlocked decisions, targetable wars, claims/cores, scripted AI strategy, rail/supply networks, ports, dockyards, escalation missions, leader/state identity, and route-specific end states.

Reward disconnection from mechanics:

- 358 focuses had expansion/front/border/claim/war/reconquest signals in ID/body.
- 285 of those 358 did not have a hard expansion payoff in the focus reward itself, using this scan set: `create_wargoal`, `declare_war_on`, `add_state_claim`, `add_state_core`, `add_claim_by`, `add_core_of`, `soviet_collapse_apply_custom_splinter_expansion_claims`, `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`, `soviet_collapse_apply_breakaway_neighbor_conflict_plan`.
- Branch status across all 41 trees: expansion is shallow in 28 trees, partial in 7, present in only 6. This is the main mismatch with the user constraint that chaos countries must be powerful and aggressive.

## Tree-By-Tree Branch Depth Classification

Legend:

- `present`: enough signal and at least some direct/supporting mechanical payload.
- `partial`: branch exists but needs stronger payoffs, route links, or depth.
- `shallow`: branch is compressed, mostly label/helper based, or too short for a full country tree.

| Tree | Classification |
| --- | --- |
| `soviet_collapse_ukraine_focus_tree` | Political, industry, military, diplomacy, mechanics present. Expansion shallow despite IDs such as `ukr_soviet_collapse_direct_national_claims` and `ukr_soviet_collapse_black_sea_hegemony`; no direct hard expansion payoff found in this tree. |
| `soviet_collapse_breakaway_focus_tree` | Political/industry/military/diplomacy present. Expansion shallow: only `soviet_collapse_border_militia_standard` and `soviet_collapse_armed_neutrality` signals; no hard expansion payoff. |
| `soviet_collapse_internal_republic_focus_tree` | Political/industry/military/diplomacy present. Expansion shallow: many border/neighbor names, but no hard expansion payoff. |
| `soviet_collapse_baltic_focus_tree` | Political/industry/military/diplomacy present. Expansion shallow: strong defensive/border naming, no hard expansion payoff; 18 hidden focus locks. |
| `soviet_collapse_caucasus_focus_tree` | Political/industry/military/diplomacy present. Expansion shallow: pass/border route language exists, no hard expansion payoff. |
| `soviet_collapse_central_asia_focus_tree` | Mostly present; expansion partial because there is at least one hard expansion effect, but most border/pass content is still helper-based. |
| `soviet_collapse_moldova_focus_tree` | Mostly present; expansion partial. Contains Moldova route depth but mutex/pathline risks around `moldova_soviet_collapse_independent_republic_council` and `moldova_soviet_collapse_ukrainian_border_compact`. |
| `soviet_collapse_belarus_focus_tree` | Political/industry/military/diplomacy present. Expansion shallow; rail/forest logic is strong but aggressive payoff is weak. |
| `soviet_collapse_kazakhstan_focus_tree` | Broadest republic tree. Political/industry/military/diplomacy present; expansion shallow in scan despite many southern/steppe signals. It is overloaded with 28 hidden locks. |
| `FTH_soviet_collapse_focus_tree` | Present across major branches; one of the healthier custom trees. Still has 18 helper-only rewards and should gain more visible anti-puppet/commune decisions. |
| `PRA_soviet_collapse_focus_tree` | All branches shallow due 22-focus compressed design. Railway identity exists, but it needs a real rail/supply hub mechanic spine and more than repeated train rewards. |
| `TSC_soviet_collapse_focus_tree` | All branches shallow due 18-focus design. Observatory/perimeter hooks exist but need a distinct mechanic and escalation payoff. |
| `RMC_soviet_collapse_focus_tree` | All branches shallow due 18-focus design. Dead-state aggression exists in outline but needs neighbor war/claims and memorial mechanic depth. |
| `DSC_soviet_collapse_focus_tree` | All branches shallow due 18-focus design. Military/dead-congress tone is strong, but mechanics are still compact. |
| `NRF_soviet_collapse_focus_tree` | All branches shallow due 18-focus design. Naval theme exists, but needs port/fleet/convoy control mechanics instead of small convoys. |
| `ICD_soviet_collapse_focus_tree` | All branches shallow due 18-focus design. Needs dead-state congress politics and aggressive endpoint depth. |
| `BSC_soviet_collapse_focus_tree` | Political/industry/military/diplomacy/mechanics present; expansion partial. Layout currently clean after corrected coordinate scan, but 8 hidden locks and 18 helper-only rewards remain. |
| `TNC_soviet_collapse_focus_tree` | Present except expansion shallow. Needs actual neighbor wars/claims tied to its urban/oasis route. |
| `ALA_soviet_collapse_focus_tree` | Present except expansion shallow. Needs steppe aggression and cores/claims instead of mostly route language. |
| `BBH_soviet_collapse_focus_tree` | Present except expansion shallow. Needs Bashkir/steppe military expansion payoff. |
| `KRS_soviet_collapse_focus_tree` | Present except expansion shallow. Naval/Baltic worker identity exists but hard expansion is weak. |
| `UDC_soviet_collapse_focus_tree` | Present across major branches. Its command network branch is a better high-chaos template, but still has 21 helper-only rewards. |
| `SDZ_soviet_collapse_focus_tree` | Present across major branches. Archive/control mechanics are clearer than most custom trees; still needs more visible aggression. |
| `GAC_soviet_collapse_focus_tree` | Present across major branches. Has pathline risk from upward/same-row prerequisites listed below. |
| `DHC_soviet_collapse_focus_tree` | Present except expansion shallow. River/host court branch is flavorful but uses many repeated small convoy rewards. |
| `KHC_soviet_collapse_focus_tree` | Present with expansion partial. Has pathline risk from upward/same-row prerequisites listed below. |
| `FEV_soviet_collapse_focus_tree` | Present with expansion partial. Far Eastern naval/port branch exists but should be stronger and more aggressive. |
| `SZA_soviet_collapse_focus_tree` | Present except expansion shallow. Needs Siberian expansion/settlement payoff beyond helper identity. |
| `UWD_soviet_collapse_focus_tree` | Present except expansion shallow. It is a war directorate but has no hard expansion payoff in this scan. |
| `MRC_soviet_collapse_focus_tree` | Present except expansion shallow. Mountain diplomacy is present; pass control and neighbor wars need hard mechanics. |
| `IUL_soviet_collapse_focus_tree` | Present except expansion shallow. Idel-Ural route needs Volga/rail expansion payoff. |
| `BAC_soviet_collapse_focus_tree` | Present except expansion shallow. Needs stronger aggressive AI/war route. |
| `ARD_soviet_collapse_focus_tree` | Present with expansion partial. Needs route-specific claims/cores and war pressure. |
| `NLC_soviet_collapse_focus_tree` | Present across major branches. Best current northern compact candidate; port/radar/supply rewards still too small/repeated. |
| `CFR_soviet_collapse_focus_tree` | Industry and mechanics present; political present. Expansion shallow, military/diplomacy partial. Construction successor should build much more factory/infrastructure and project power through protectorates/contracts. |
| `OGB_soviet_collapse_focus_tree` | All branches shallow due 23-focus design. Needs fuller restoration politics, Volga trade/war mechanics, and regional claims. |
| `MFR_soviet_collapse_focus_tree` | Industry/military/mechanics present; expansion present; politics/diplomacy partial. Good arsenal concept, but 31 helper-only rewards and repeated arms factory focus payoffs flatten it. |
| `KZR_soviet_collapse_ancient_focus_tree` | All branches shallow due 16-focus compact ancient design. Has claims/wargoal but needs real political/industry/military/diplomacy branches. |
| `SOG_soviet_collapse_ancient_focus_tree` | All branches shallow due 16-focus compact design. Needs Sogdian merchant/diplomatic mechanics and broader city-state payoff. |
| `KHW_soviet_collapse_ancient_focus_tree` | All branches shallow due 16-focus compact design. Irrigation/water identity needs a mechanical spine. |
| `ALN_soviet_collapse_ancient_focus_tree` | All branches shallow due 16-focus compact design. Pass control identity needs supply/pass war mechanics. |

## Pathline and Layout Risks

Corrected coordinate scan:

- Duplicate absolute `(x, y)` coordinates: 0 groups.
- Nested focus blocks: 0.
- Same-row/upward prerequisites: 6.
- Mutually exclusive pairs: 90.
- Mutually exclusive near-overlap/pathline risk: 2 pair entries.
- Hidden `available = { has_completed_focus = ... }` locks: 301 focuses.

Same-row/upward prerequisite risks to patch first:

- `GAC_rural_congress_charter` at `(18, 7)` requires `GAC_harvest_truce_guarantees` at `(4, 11)`.
- `GAC_winter_hay_roads` at `(10, 9)` requires `GAC_seed_and_rifle_stores` at `(4, 9)`.
- `GAC_winter_hay_roads` at `(10, 9)` requires `GAC_field_hospital_barns` at `(8, 9)`.
- `KHC_stanitsa_autonomy_statute` at `(8, 8)` requires `KHC_grain_passage_guarantees` at `(11, 11)`.
- `KHC_endgame` at `(8, 10)` requires `KHC_grain_passage_guarantees` at `(11, 11)`.
- `KHC_endgame` at `(8, 10)` requires `KHC_steppe_and_mountain_compact` at `(12, 10)`.

Mutual exclusion near-overlap/pathline risk:

- `moldova_soviet_collapse_independent_republic_council` at `(11, 4)` is mutually exclusive with `moldova_soviet_collapse_ukrainian_border_compact` at `(12, 3)`. This likely draws a line through or beside the fork in a confusing way.

Hidden `available = has_completed_focus` route locks by file:

- Republics: 132.
- Custom splinters: 151.
- Factory successors: 18.
- Ancient restorations: 0.

Worst hidden-lock trees:

- `soviet_collapse_kazakhstan_focus_tree`: 28.
- `soviet_collapse_baltic_focus_tree`: 18.
- `soviet_collapse_caucasus_focus_tree`: 17.
- `UWD_soviet_collapse_focus_tree`: 17.
- `IUL_soviet_collapse_focus_tree`: 17.
- `soviet_collapse_moldova_focus_tree`: 15.
- `soviet_collapse_ukraine_focus_tree`: 13.
- `soviet_collapse_central_asia_focus_tree`: 13.
- `DHC_soviet_collapse_focus_tree`: 13.
- `MFR_soviet_collapse_focus_tree`: 13.

The hidden locks are not necessarily invalid, but they are graph-hostile. Where the relationship is genuinely route progression, prefer visible prerequisites/mutual exclusions. Keep `available` for dynamic world-state gates, tag checks, or pressure gates that should not draw a line.

## Priority Implementation Plan for Parent

1. Patch hard layout risks first:
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
   - IDs: `GAC_rural_congress_charter`, `GAC_winter_hay_roads`, `KHC_stanitsa_autonomy_statute`, `KHC_endgame`.
   - Payoff: prevents pathlines from running backward/upward through branches while parent edits release/scenario mechanics.

2. Patch the Moldova mutual exclusion fork:
   - File: `common/national_focus/005_soviet_collapse_republics.txt`.
   - IDs: `moldova_soviet_collapse_independent_republic_council`, `moldova_soviet_collapse_ukrainian_border_compact`.
   - Payoff: keep route choice readable; move lanes or change prerequisite anchor so mutual-exclusion line does not run through nearby focuses.

3. Rework high-chaos aggression before polishing ordinary republics:
   - Files: `005_soviet_collapse_custom_splinters.txt`, `005_soviet_collapse_factory_successors.txt`, `005_soviet_collapse_ancient_restorations.txt`.
   - Priority IDs/trees: `PRA_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`, `CFR_soviet_collapse_focus_tree`, `MFR_soviet_collapse_focus_tree`, ancient trees `KZR/SOG/KHW/ALN`.
   - Payoff: meets user constraint that chaos countries are powerful/aggressive. Use hard claims/cores/wargoals, aggressive AI strategies, postwar settlement decisions, and route-specific neighbor conflicts.

4. Give special-purpose tags their required mechanical spines:
   - `PRA`: rail authority, rail/supply hub construction, armored train/supply decisions, corridor war goals.
   - `NRF`: naval bases, dockyards, convoy/port seizure decisions, White Sea/Arctic naval aggression.
   - `CFR`: large-scale factories/infrastructure, construction directorate decisions, client-city/protectorate mechanics.
   - `MFR`: production surge risks, arms export/recognition mechanics, direct militarized expansion.
   - `KHW`/`ALN`: irrigation/pass-control supply mechanics.

5. Reduce helper-only focus completion sameness:
   - Do not remove shared helpers where they centralize variables or AI pressure.
   - Add one visible payoff per route node cluster: decision unlock, state target, war/claim/core, unit template, AI strategy, dynamic mission, named map construction, or diplomatic relation/faction action.
   - Start with trees over 20 helper-only rewards: `MFR`, `CFR`, `DHC`, `BAC`, `SDZ`, `GAC`, `FEV`, `SZA`, `IUL`, `UWD`, `KHC`, `MRC`, `UDC`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_kazakhstan_focus_tree`, `soviet_collapse_ukraine_focus_tree`.

6. Convert hidden route locks into visible graph structure:
   - First targets: Kazakhstan, Baltic, Caucasus, UWD, IUL, Moldova, Ukraine.
   - Keep dynamic world-state gates in `available`, but move focus-to-focus route gates into prerequisites/mutual exclusions where possible.

## Validation

Commands/checks run:

- Parsed all four focus files for focus tree count, focus count, rewards, coordinates, prerequisites, mutual exclusions, and hidden locks.
- Brace balance scan: passed for all four files.
- Unsupported operator scan: `rg -n "<=|>="` over the four focus files returned no matches.
- `rg -n "add_ideas"` over the four focus files returned no matches.
- `git diff --check -- docs/plans/005_soviet_collapse_plans/subagent_handoffs/20260605_082725_focus_tree_auditor_event005_current_readonly_audit.md`: passed.

Skipped:

- No gameplay-file `git diff --check` was needed because no gameplay patches were made. It should still be run by the parent after integration patches.
- No in-game validation. This was a static subagent audit.

## Changes Made

Created this handoff report only:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/20260605_082725_focus_tree_auditor_event005_current_readonly_audit.md`

No focus-tree patches were made. No flags were touched.

## Remaining Risks

This is not a completion claim. The full rework objective remains incomplete until all Soviet Collapse focus trees have route-specific political, industrial, expansion, military/diplomacy, and special-mechanic branches with visible payoffs, aggressive AI behavior, and clean pathlines.
