# Event005 Soviet Collapse Focus Tree Audit

Role: `chaosx_focus_tree_auditor`

Date: 2026-06-05 14:38 UTC

Scope: read-only audit of:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`

No focus, localisation, gfx, flag, sprite, or idea files were edited.

## References Consulted

Offline Paradox wiki pages opened before inspecting target files:

- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
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

Vanilla references consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`

Relevant reference implications:

- Focus coordinates use grid units; `y` should generally move downward through prerequisite chains.
- Prerequisites create visible path lines, so wide same-level fanouts are readability risks even if valid.
- `ai_will_do` is an MTTH block and should be route-aware for major choices.
- `add_ideas`, `swap_ideas`, `create_wargoal`, `add_state_claim`, `add_state_core`, `add_ai_strategy`, construction effects, and decision unlock tooltips are all valid focus reward surfaces but should not be used as interchangeable filler.

## 1. Focus Counts

### By file

| File | Focus count |
| --- | ---: |
| `005_soviet_collapse_republics.txt` | 501 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 |
| `005_soviet_collapse_factory_successors.txt` | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 |
| **Total audited focus count** | **1698** |

### By tree

| File | Tree | Line | Focuses |
| --- | --- | ---: | ---: |
| republics | `soviet_collapse_ukraine_focus_tree` | 18 | 83 |
| republics | `soviet_collapse_breakaway_focus_tree` | 2313 | 36 |
| republics | `soviet_collapse_internal_republic_focus_tree` | 3125 | 62 |
| republics | `soviet_collapse_baltic_focus_tree` | 4645 | 42 |
| republics | `soviet_collapse_caucasus_focus_tree` | 5608 | 40 |
| republics | `soviet_collapse_central_asia_focus_tree` | 6529 | 45 |
| republics | `soviet_collapse_moldova_focus_tree` | 7665 | 48 |
| republics | `soviet_collapse_belarus_focus_tree` | 8807 | 53 |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 10113 | 92 |
| custom splinters | `FTH_soviet_collapse_focus_tree` | 15 | 47 |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 1222 | 22 |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 1857 | 18 |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 2367 | 18 |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 2843 | 18 |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 3377 | 18 |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 3881 | 18 |
| custom splinters | `BSC_soviet_collapse_focus_tree` | 4349 | 47 |
| custom splinters | `TNC_soviet_collapse_focus_tree` | 5493 | 47 |
| custom splinters | `ALA_soviet_collapse_focus_tree` | 6628 | 47 |
| custom splinters | `BBH_soviet_collapse_focus_tree` | 7739 | 47 |
| custom splinters | `KRS_soviet_collapse_focus_tree` | 8933 | 47 |
| custom splinters | `UDC_soviet_collapse_focus_tree` | 10158 | 47 |
| custom splinters | `SDZ_soviet_collapse_focus_tree` | 11366 | 47 |
| custom splinters | `GAC_soviet_collapse_focus_tree` | 12616 | 47 |
| custom splinters | `DHC_soviet_collapse_focus_tree` | 13783 | 47 |
| custom splinters | `KHC_soviet_collapse_focus_tree` | 14982 | 47 |
| custom splinters | `FEV_soviet_collapse_focus_tree` | 16147 | 47 |
| custom splinters | `SZA_soviet_collapse_focus_tree` | 17338 | 47 |
| custom splinters | `UWD_soviet_collapse_focus_tree` | 18507 | 47 |
| custom splinters | `MRC_soviet_collapse_focus_tree` | 19694 | 47 |
| custom splinters | `IUL_soviet_collapse_focus_tree` | 20867 | 47 |
| custom splinters | `BAC_soviet_collapse_focus_tree` | 22007 | 47 |
| custom splinters | `ARD_soviet_collapse_focus_tree` | 23140 | 47 |
| custom splinters | `NLC_soviet_collapse_focus_tree` | 24339 | 47 |
| factory successors | `CFR_soviet_collapse_focus_tree` | 18 | 47 |
| factory successors | `OGB_soviet_collapse_focus_tree` | 1018 | 23 |
| factory successors | `MFR_soviet_collapse_focus_tree` | 1579 | 58 |
| ancient restorations | `KZR_soviet_collapse_ancient_focus_tree` | 13 | 16 |
| ancient restorations | `SOG_soviet_collapse_ancient_focus_tree` | 423 | 16 |
| ancient restorations | `KHW_soviet_collapse_ancient_focus_tree` | 827 | 16 |
| ancient restorations | `ALN_soviet_collapse_ancient_focus_tree` | 1235 | 16 |

## 2. Idea Reward Audit

No direct focus reward was found adding the same `add_ideas` idea multiple times in the same focus block. No direct focus reward was found adding a long list of ideas via direct `add_ideas` statements.

The remaining idea-spam concern is helper-mediated and lifecycle/design-level:

- `common/scripted_effects/005_soviet_collapse_effects.txt:8248` `soviet_collapse_update_pra_authority_idea`
  - Called from `PRA_the_timetable_declares_authority` at `custom_splinters.txt:1242`
  - Called from `PRA_armored_train_directorate` at `custom_splinters.txt:1430`
  - Called from `PRA_passport_of_the_moving_state` at `custom_splinters.txt:1612`
  - Called from `PRA_league_transit_bargain` at `custom_splinters.txt:1680`
  - Helper adds or ensures `pra_timetable_sovereignty_board`.
  - Risk: repeated calls are probably intended as staged updates, but the player-facing reward can still read as "another authority idea tick" unless the idea visibly changes or the focus tooltip describes the route effect.

- `common/scripted_effects/005_soviet_collapse_effects.txt:17898` `soviet_collapse_update_dsc_dead_army_idea`
  - Called from `DSC_call_the_dead_soldiers_congress` at `custom_splinters.txt:2873`
  - Helper adds or ensures `dsc_dead_army_politics`.
  - Risk: this is not repeated in focuses, but it is another national-spirit-centric route identity.

- Setup helpers seed many starting national spirits outside focus rewards, for example `soviet_collapse_setup_cfr_successor` at `effects.txt:18384`, `soviet_collapse_setup_mfr_successor` at `effects.txt:18404`, `soviet_collapse_setup_dsc_successor` at `effects.txt:18522`, `soviet_collapse_setup_ogb_successor` at `effects.txt:18781`, `soviet_collapse_setup_pra_successor` at `effects.txt:18911`, `soviet_collapse_setup_nrf_successor` at `effects.txt:18990`, and `soviet_collapse_setup_nlc_successor` at `effects.txt:19013`.
  - This is not a direct focus duplicate issue, but it does mean many trees start with spirit identity and then repeatedly route through focus helpers that alter variables, decisions, or flags. Parent should verify that each starting spirit has a clear lifecycle, not just permanent flavor.

## 3. Repeated Reward-Helper Hotspots

These helpers are not technically duplicate idea spam, but they are major generic-reward hotspots. Their high call counts explain why many focus rewards feel shallow or interchangeable despite large focus counts.

| Helper | Calls | Helper line | Payload summary | Audit risk |
| --- | ---: | ---: | --- | --- |
| `soviet_collapse_apply_focus_depot_and_supply_control` | 142 | `effects.txt:9289` | Variable changes | Generic logistics reward used across too many unrelated countries. |
| `soviet_collapse_apply_focus_military_consolidation` | 131 | `effects.txt:9268` | Variable changes | Generic military reward used across political, army, and expansion nodes. |
| `soviet_collapse_apply_focus_legal_recognition` | 108 | `effects.txt:9168` | Variable changes | Generic legitimacy reward; risks making political branches feel like counters. |
| `soviet_collapse_apply_focus_republican_compact_plan` | 95 | `effects.txt:9940` | Variable changes | Widely used as route payoff without enough visible end-state distinction. |
| `soviet_collapse_apply_focus_foreign_channel` | 66 | `effects.txt:11186` | Variable change | Generic diplomacy reward. |
| `soviet_collapse_apply_focus_security_supply_plan` | 65 | `effects.txt:9967` | Variable changes | Generic security/logistics reward. |
| `soviet_collapse_apply_objective_source_pressure_delta` | 61 | `effects.txt:1743` | Large variable pressure helper | Mechanically useful, but invisible if not paired with tailored tooltip or objective outcome. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 54 | `effects.txt:11514` | Flag, variables, AI strategy | High-chaos identity may feel generic when repeated across many tags. |
| `soviet_collapse_apply_focus_league_preparation` | 51 | `effects.txt:9887` | Variable changes | League path risks becoming a repeated support lane. |
| `soviet_collapse_apply_focus_chaos_assault_plan` | 50 | `effects.txt:10271` | Variable changes | Aggressive route helper is common, but not always paired with specific war/claim consequences. |
| `soviet_collapse_apply_high_chaos_neighbor_expansion_plan` | 25 | `effects.txt:10129` | 1 war goal, 2 AI strategies | Strong generic aggression payload. Good for OP chaos countries, risky if used without country-specific target logic. |
| `soviet_collapse_spawn_custom_splinter_assault_columns_payload` | 23 | `effects.txt:8567` | 2 unit spawns | Strong repeated military payoff. Needs anti-loop and route-lock verification. |
| `soviet_collapse_apply_custom_splinter_expansion_claims_payload` | 11 | `effects.txt:8658` | 2 war goals, 4 AI strategies, variable change | Strong but very generic expansion payload. |

Recommendation: keep the helpers, but parent should wrap major branch endpoints with country-specific visible payloads: unique decision unlocks, named state construction, claims/cores with postwar handling, route-specific AI, and idea upgrades only when the idea changes role.

## 4. Layout And Pathline Risks

The layout parser found several categories of risk.

### Duplicate or too-close coordinates

- `soviet_collapse_belarus_focus_tree`
  - `blr_soviet_collapse_league_supply_timetables` at `republics.txt:9343`
  - `blr_soviet_collapse_prepare_league_freight_tables` at `republics.txt:9765`
  - Parsed absolute coordinate duplicate: `(17,12)`.
  - Action: move one of these one or two columns away and re-check prereqs around `blr_soviet_collapse_join_the_league_when_war_comes` at `republics.txt:9798` and `blr_soviet_collapse_the_green_rail_pact` at `republics.txt:10040`.

- Same-row spacing risks detected in:
  - Ukraine: `ukr_soviet_collapse_republican_deep_battle` at `republics.txt:1125` near `ukr_soviet_collapse_advisers_without_flags` at `republics.txt:1445`.
  - Central Asia: `central_asia_soviet_collapse_desert_scout_columns` at `republics.txt:6921` near `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` at `republics.txt:7429`.
  - Moldova: `moldova_soviet_collapse_river_guard_brigades` at `republics.txt:7886` near `moldova_soviet_collapse_ukrainian_grain_road` at `republics.txt:8005`.
  - Kazakhstan: many same-row adjacent nodes, especially around `kaz_soviet_collapse_the_alash_courts` at `republics.txt:10358`, `kaz_soviet_collapse_the_steppe_arsenal` at `republics.txt:10571`, `kaz_soviet_collapse_no_concession_without_a_republic` at `republics.txt:10887`, and `kaz_soviet_collapse_copper_and_chrome_ledgers` at `republics.txt:11650`.
  - MFR: `MFR_rifles_before_speeches` at `factory_successors.txt:1973`, `MFR_workers_must_not_flee` at `factory_successors.txt:2495`, and `MFR_builders_waste_steel` at `factory_successors.txt:2517` are too close on the same row.

### Wide parent-child spans

Wide spans are not syntax errors, but they create the exact "scattered" look the user complained about. High-value examples:

- Ukraine:
  - `ukr_soviet_collapse_open_the_liaison_offices` at `republics.txt:228` is reached through a line from `ukr_soviet_collapse_foreign_courts_notice_kyiv` and then fans into very wide foreign/diplomatic child lanes.
  - `ukr_soviet_collapse_foreign_advisers_in_plain_coats` at `republics.txt:1055` has a 12-column span from `ukr_soviet_collapse_open_the_liaison_offices`.
  - `ukr_soviet_collapse_protectorate_debate` at `republics.txt:1691` has an 11-column span from `ukr_soviet_collapse_open_the_liaison_offices`.
  - `ukr_soviet_collapse_when_the_fields_refuse_the_state` at `republics.txt:2287` links across the bread-state/high-chaos cluster.

- Republic generic tree:
  - `soviet_collapse_guard_the_radio_stations` at `republics.txt:2356` spans 6 columns from the root.
  - `soviet_collapse_the_republic_defines_itself` at `republics.txt:2449` spans 6 columns from the root.
  - `soviet_collapse_depots_choose_flags_branch` at `republics.txt:2816` spans 10 columns from `soviet_collapse_secure_ministry_ledgers`.

- CFR:
  - `CFR_the_concrete_committee` at `factory_successors.txt:188` spans 10 columns from `CFR_the_unfinished_city_speaks`.
  - `CFR_a_civilian_factory_in_every_capital` at `factory_successors.txt:510` and `CFR_the_debt_map` at `factory_successors.txt:535` create a far-right/far-left merge into the late construction branch.

- FEV:
  - `FEV_endgame` at `custom_splinters.txt:17284` has a large fan-in from nine prerequisites, including `FEV_extreme_path`, `FEV_settlement`, `FEV_authority_from_the_harbor`, `FEV_vladivostok_harbor_board`, `FEV_razdolnoye_rear_area`, `FEV_far_eastern_staff_map`, `FEV_amur_buffer_posts`, `FEV_pacific_between_empires`, and `FEV_no_foreign_command_on_the_line`.
  - This is structurally meaningful but visually noisy. Parent should split it into two or three visible capstones or convert some gates to `available` checks with custom tooltips.

### Same-row mutual exclusions

The user explicitly does not want meaningless mutual exclusion symbols or visually messy lines. Current notable risks:

- `MFR_officers_chair_the_board` at `factory_successors.txt:1706` mutually excludes `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, and `MFR_eternal_arsenal`; spans reach 10-22 columns.
- `MFR_armorers_elect_delegates` at `factory_successors.txt:1735` mutually excludes `MFR_merchants_of_ammunition` and `MFR_eternal_arsenal`; spans 8-12 columns.
- `GAC_settlement` / `GAC_radical_turn`, `DHC_settlement` / `DHC_radical_turn`, `KHC_settlement` / `KHC_radical_turn`, and `ARD_settlement` / `ARD_radical_turn` are same-row, 6-7 column mutual exclusions in `custom_splinters.txt`.
- Ancient restorations use same-row symbolic/expansionist exclusions:
  - `KZR_symbolic_crossing_state` / `KZR_expansionist_steppe_levy` at `ancient_restorations.txt:210` and `:239`
  - `SOG_symbolic_city_league` / `SOG_expansionist_merchant_claims` at `:619` and `:647`
  - `KHW_symbolic_oasis_authority` / `KHW_expansionist_water_claims` at `:1018` and `:1045`
  - `ALN_symbolic_pass_principality` / `ALN_expansionist_mountain_claims` at `:1427` and `:1453`
  - These are lore-meaningful choices, but the same-row long-line presentation still risks visual clutter.

### Continuous focus panel overlap

Continuous focus positions are set far to the right or high in pixel space:

- Ancient: `continuous_focus_position = { x = 2304 y = 140 }`
- Custom splinters commonly use `x = 2880 y = 180`
- CFR uses `x = 3360 y = 180`
- OGB uses `x = 1728 y = 180`

No direct continuous-focus panel overlap was proven by static coordinate parsing. Parent should still check CFR and Kazakhstan in-game because their visible trees are wide and late branches extend far right.

## 5. Branch-Depth Assessment

### Ukraine

Status: broad and mechanically richer than the shared trees, but still visually scattered.

Strengths:

- Political branch exists around `ukr_soviet_collapse_question_of_statehood`, `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, and `ukr_soviet_collapse_officers_above_parties`.
- Industry/logistics branch exists around grain, depots, Dnieper workshops, Black Sea ports, and bread-state mechanics.
- Expansion/diplomacy exists through League, Romanian/Black Sea, protectorate, national claims, border arbitration, and bread-state/high-chaos branches.

Risks:

- Branches are too interwoven visually. The foreign branch (`ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, `ukr_soviet_collapse_protectorate_debate`) drifts far right and crosses other military/Black Sea content.
- The bread-state/high-chaos cluster has meaningful mechanics but its late prereqs are hard to read.

Assessment: depth is present; layout and visible route grouping need cleanup.

### Belarus

Status: medium-large, with a railway/League identity, but current layout has a concrete duplicate-coordinate defect and dense pathline risk.

Strengths:

- Distinct rail and League logistics identity is visible through `blr_soviet_collapse_league_supply_timetables`, `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_the_green_rail_pact`, and `blr_soviet_collapse_the_league_depot_at_minsk`.
- The tree has political and military support content.

Risks:

- Duplicate coordinate between `blr_soviet_collapse_league_supply_timetables` and `blr_soviet_collapse_prepare_league_freight_tables`.
- Several rail/League nodes are compressed or cross-connected enough to make the route look messy rather than like a clear railway-state branch.

Assessment: good identity, but layout defect should be a parent priority.

### Kazakhstan

Status: largest and most ambitious tree in this audit at 92 focuses, with real political, industry/resource, military, diplomacy, and expansion lanes.

Strengths:

- Political routes include Alash, socialist steppe, state-across-distance, and high-chaos old-steppe memory.
- Industry/resource branch is real: `kaz_soviet_collapse_karaganda_emergency_board`, `kaz_soviet_collapse_oil_field_protection_orders`, `kaz_soviet_collapse_rail_to_the_mines`, `kaz_soviet_collapse_resource_concessions_debate`, `kaz_soviet_collapse_industrial_settlement_compacts`, and `kaz_soviet_collapse_resource_sovereignty`.
- Expansion/federation branch exists: southern guarantees, steppe federation, arbitration court, southern republics writing together, Caspian/security/border content.

Risks:

- Too many lanes use generic helpers and adjacent rows. The tree has depth, but visual density makes it hard to parse.
- Several same-row close pairs and wide spans around resource, Alash, and southern federation nodes need layout work.

Assessment: depth is strong; readability and payoff differentiation remain the main risks.

### Regional republics

Includes breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova.

Status: uneven.

Strengths:

- All have at least political, military/security, foreign/League, and some economic/logistics hooks.
- Moldova and Central Asia now have route-specific mechanic hooks and decision tooltips in places.

Risks:

- `soviet_collapse_breakaway_focus_tree` remains visually broad from the root, and generic helper use makes it feel like a template.
- Baltic/Caucasus/Central Asia/Moldova use repeated helper vocabulary heavily, so branch names differ more than reward behavior.
- Central Asia has a direct claim-dump risk: `central_asia_soviet_collapse_khwarazm_restoration_debate` at `republics.txt:7482` gives 7 claims through its reward block.

Assessment: playable scaffold exists, but several trees still lack bespoke political/industry/expansion separation as felt gameplay.

### Custom splinters

Status: mixed. The 47-focus custom splinters have a recognizable template; 18-focus high-chaos/death-state splinters are compact but stronger mechanically.

Strengths:

- Many custom splinters now have settlement/radical forks, industry plans, war plans, diplomatic plans, and endgames.
- PRA is a standout compact tree with rail authority, corridor construction, units, diplomacy, and expansion.
- FEV has a broad branch spread with military, economy, diplomacy, industry, hidden doctrine, and endgame gates.

Risks:

- Shared helper identity is very visible. Many trees use the same sequence of `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `inner_faction`, `settlement`, `radical_turn`, `industry_plan`, `hidden_doctrine`, `extreme_gate`, `endgame`.
- The route architecture is often real on paper but still feels template-driven because the reward helpers repeat.

Assessment: broad coverage, but many branches still need country-specific mechanical payoffs to stop feeling like reskinned templates.

### Factory successors

Status: deepest family after Kazakhstan, but visually messy in MFR and still narrow in OGB.

Strengths:

- CFR has a strong construction-state identity with decisions, construction buildout, foreign contracts, coercive city-building, and late rebuild/expansion.
- MFR has unusually deep arms-market, production, political control, client network, and OP war-market content.
- OGB has a compact restoration/Volga identity with claims, future-Bulgaria routing, and a final war payoff.

Risks:

- CFR has wide spans and far-right branch drift.
- MFR's four-way mutually exclusive rifle ownership route is visually messy and has too many same-row long mutex lines.
- OGB is only 23 focuses and still lacks a full industrial branch distinct from Volga trade/logistics.

Assessment: CFR and MFR are strong but need layout cleanup; OGB needs branch depth, especially industry and postwar integration.

### Ancient restorations

Status: compact and thematic, but shallow.

Strengths:

- Each has symbolic/restoration and expansion choice.
- Each has old-border files and final war/survival/endgame hooks.

Risks:

- 16 focuses per tree is too shallow for the user's requested aggressive/overpowered chaos-country trees.
- `KZR_old_border_files`, `SOG_old_city_border_files`, `KHW_old_oasis_border_files`, and `ALN_old_pass_border_files` are direct claim-dump nodes with 4-5 claims plus decision unlocks.
- Political, industry, and expansion branches are not distinct enough; industry is mostly a few workshop/road/support nodes.

Assessment: good flavor skeleton, insufficient depth for full branch families.

## 6. Chaos-Country OP/Aggression Assessment

### CFR

File: `factory_successors.txt`, tree line 18, 47 focuses.

Strengths:

- Strong construction identity and several decision unlocks: `CFR_the_trust_office_takes_the_seal` at `:48`, `CFR_emergency_cement_accounts` at `:88`, `CFR_rails_first` at `:326`, `CFR_a_civilian_factory_in_every_capital` at `:510`, `CFR_the_state_that_builds` at `:776`.
- Concrete expansion route exists through `CFR_the_builder_state_marches_east` at `:820`, `CFR_build_the_border_bend_the_border` at `:845`, `CFR_factories_as_embassies` at `:865`, and `CFR_reconstruction_protectorates` at `:888`.

Risk:

- OP aggression is more construction/economic snowball than direct war. If user expects chaos-country aggression, parent should add targeted border pressure, protectorate ultimatums, and AI conquer/antagonize hooks to late builder-state branches.

### DSC

File: `custom_splinters.txt`, tree line 2843, 18 focuses.

Strengths:

- Very aggressive opening: `DSC_call_the_dead_soldiers_congress` at `:2848` uses `soviet_collapse_spawn_custom_splinter_assault_columns_payload`, `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`, and high-chaos identity.
- `DSC_congress_of_the_dead_army` at `:3293` has direct `create_wargoal`, 2 AI strategies, and 2 decision unlocks.
- `soviet_collapse_dsc_launch_dead_army_neighbor_wars` in effects uses neighbor war goals and 250-value conquer/antagonize AI.

Risk:

- Strong but compact. Needs a deeper method branch: living witnesses vs revenant command should affect targets, unit types, occupation/integration, and failure states.

### PRA

File: `custom_splinters.txt`, tree line 1222, 22 focuses.

Strengths:

- Distinct rail authority mechanic through `soviet_collapse_update_pra_authority_idea`, `soviet_collapse_build_pra_corridor_network`, and rail guard columns.
- Expansion endpoint `PRA_rails_over_capitals` at `:1754` has war goal, AI conquer/antagonize, decision unlock, unit/building support, and `soviet_collapse_complete_pale_railway_endgame`.
- Strong identity without needing a large tree.

Risk:

- Authority idea calls may feel repetitive. Parent should ensure every stage visibly changes the railway authority instead of re-adding the same board.

### MFR

File: `factory_successors.txt`, tree line 1579, 58 focuses.

Strengths:

- Deepest factory successor. Has a political ownership fork, production branch, client arms branch, late arsenal-state route, and direct war-market aggression.
- `MFR_no_peace_without_orders` at `:2853` has war goal, 2 AI strategies, decision unlock, and offsite factory.
- `MFR_every_order_a_rifle` at `:2900` has 3 AI strategies.
- `MFR_eternal_arsenal_marches` at `:2926` has war goal, 4 AI strategies, and offsite factory.

Risk:

- Path lines are messy. The four-way mutual exclusion at `MFR_who_owns_the_rifle` is lore-important, but the current same-row and wide-spanning mutex presentation is visually noisy.

### NRF

File: `custom_splinters.txt`, tree line 3377, 18 focuses.

Strengths:

- Strong high-chaos naval/dead-fleet identity.
- `NRF_northern_revenant_fleet` at `:3815` has war goal, 2 AI strategies, decision unlock, expansion claims helper, assault columns helper, and revenant endgame helper.

Risk:

- Too compact for a full chaos-country tree. Needs deeper naval OP mechanics: ghost convoy raiding, port seizure decisions, Arctic intervention targets, naval invasion preparation, and postwar port integration.

### FEV

File: `custom_splinters.txt`, tree line 16147, 47 focuses.

Strengths:

- Has political, military, economy, foreign, League, industry, war, hidden doctrine, and endgame lanes.
- `FEV_harbor_fortress_line` at `:16704`, `FEV_war_plan` at `:16785`, `FEV_extreme_path` at `:17199`, and `FEV_pacific_between_empires` at `:17246` provide aggression and diplomacy surfaces.

Risk:

- The endgame at `FEV_endgame` line `:17284` has a nine-prereq fan-in and no direct war/claim payload in the focus itself. Aggression is distributed earlier, making the capstone read less OP than DSC/PRA/MFR/NRF.

### OGB

File: `factory_successors.txt`, tree line 1018, 23 focuses.

Strengths:

- The restoration identity is clear.
- `OGB_the_old_name_survives_modern_war` at `:1533` has direct war goal and 2 AI strategies.
- `soviet_collapse_apply_ogb_volga_trade_city_claims` at `effects.txt:17652` is called from `OGB_the_volga_cannot_have_two_seals`, `OGB_answer_the_idel_ural_question`, and `OGB_claim_the_old_trade_cities`, and includes war/AI handling.

Risk:

- Too small and too narrow. Needs a real industry/trade branch and postwar Volga/Kazan/Ufa integration mechanics, otherwise it remains a flavorful restoration lane rather than an OP chaos-country tree.

## 7. Prioritized Parent Patch List

1. Fix the Belarus duplicate coordinate and rail/League pathline cluster.
   - Touch focus IDs: `blr_soviet_collapse_league_supply_timetables`, `blr_soviet_collapse_prepare_league_freight_tables`, `blr_soviet_collapse_join_the_league_when_war_comes`, `blr_soviet_collapse_the_green_rail_pact`, `blr_soviet_collapse_the_league_depot_at_minsk`.
   - Recommended change: move `prepare_league_freight_tables` one row/column into a clear rail branch and route League freight prerequisites through a visible rail spine.

2. Rework MFR's four-way mutual exclusion presentation.
   - Touch focus IDs: `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, `MFR_eternal_arsenal`.
   - Recommended change: use a compact diamond or vertical route selector with only lore-important mutex symbols; avoid 8-22 column mutex spans.

3. Split or simplify `FEV_endgame` fan-in.
   - Touch focus IDs: `FEV_endgame`, `FEV_extreme_path`, `FEV_settlement`, `FEV_authority_from_the_harbor`, `FEV_vladivostok_harbor_board`, `FEV_razdolnoye_rear_area`, `FEV_far_eastern_staff_map`, `FEV_amur_buffer_posts`, `FEV_pacific_between_empires`, `FEV_no_foreign_command_on_the_line`.
   - Recommended change: make two capstones, one Pacific diplomatic/league and one extreme war-state, then a final optional unifying focus gated by `available` checks instead of every visible prerequisite.

4. Add OP aggression/postwar handling to OGB.
   - Touch focus IDs: `OGB_the_volga_cannot_have_two_seals`, `OGB_answer_the_idel_ural_question`, `OGB_claim_the_old_trade_cities`, `OGB_future_bulgaria_file`, `OGB_the_old_name_survives_modern_war`.
   - Recommended mechanics: Volga trade-city integration decisions, Kazan/Ufa occupation or compact route, temporary resistance penalties, cores after integration missions, and AI conquer/antagonize toward Idel-Ural only when valid.

5. Deepen NRF beyond the 18-focus compact structure.
   - Touch focus IDs: `NRF_revenant_admiralty`, `NRF_salvage_the_dark_berths`, `NRF_ghost_convoy_escorts`, `NRF_claim_the_white_sea_lane`, `NRF_fleet_that_does_not_dock`, `NRF_northern_revenant_fleet`.
   - Recommended mechanics: Arctic port seizure decisions, convoy raiding missions, naval-base buildout, special marine/ghost convoy units, and postwar port integration.

6. Reduce ancient restoration claim dumps.
   - Touch focus IDs: `KZR_old_border_files`, `SOG_old_city_border_files`, `KHW_old_oasis_border_files`, `ALN_old_pass_border_files`, plus `central_asia_soviet_collapse_khwarazm_restoration_debate`.
   - Recommended mechanics: split claim discovery from claim activation; use decisions or missions to validate border claims and add integration/postwar handling.

7. Give custom splinter 47-focus templates more bespoke payoffs.
   - Priority tags: `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`.
   - Recommended mechanics: replace some generic calls to `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, and `soviet_collapse_apply_focus_legal_recognition` with tag-specific state construction, targeted decisions, route AI, and unique mission unlocks.

8. Clean Ukraine's far-right diplomatic/foreign branch.
   - Touch focus IDs: `ukr_soviet_collapse_open_the_liaison_offices`, `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, `ukr_soviet_collapse_protectorate_debate`, `ukr_soviet_collapse_equipment_corridor_authority`, `ukr_soviet_collapse_ports_need_soldiers`.
   - Recommended change: group foreign liaison nodes into a vertical diplomatic branch and move Black Sea/port military nodes into a separate military-expansion branch.

9. Give CFR more aggressive external leverage if it is meant to be OP.
   - Touch focus IDs: `CFR_the_builder_state_marches_east`, `CFR_build_the_border_bend_the_border`, `CFR_factories_as_embassies`, `CFR_reconstruction_protectorates`, `CFR_rebuild_russia_without_moscow`.
   - Recommended mechanics: construction protectorate ultimatums, border permit coercion decisions, AI antagonize/conquer targets conditioned on neighbors, and postwar reconstruction client states.

10. Turn repeated helper rewards into visible branch payoffs.
   - Hot helpers: `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_republican_compact_plan`, `soviet_collapse_apply_focus_foreign_channel`.
   - Recommended pattern: keep the variable helper as backend, but pair branch endpoints with one visible payload from: decision tier unlock, named state construction, special unit, claim/war/diplomacy consequence, route-specific AI strategy, or idea upgrade.

## 8. Validation Commands Run

Commands and checks run:

- `rg --files paradox_wiki -g '*National focus*' -g '*Data structures*' -g '*Triggers*' -g '*Effects*' -g '*Modifiers*' -g '*Localisation*' -g '*Scopes*' -g '*Decision modding*' -g '*Idea modding*' -g '*AI modding*'`
- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`
- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/chaos-redux-subagents/SKILL.md`
- `sed -n` reads of all required offline wiki pages listed above.
- `rg --files '/home/klim/projects/Hearts of Iron IV/documentation' -g '*focus*' -g '*effects*' -g '*triggers*' -g '*script*'`
- `rg -n` checks in `effects_documentation.md` for `add_ideas`, `swap_ideas`, `load_focus_tree`, `create_wargoal`, `add_state_claim`, `add_state_core`, `add_ai_strategy`, construction, unit, decision, and politics effects.
- `rg -n` checks in `triggers_documentation.md` for `has_completed_focus`, focus tree, idea, government, war, and state-control triggers.
- `sed -n '1,220p' '/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt'`
- `rg -n` broad scan of focus rewards, ids, tree ids, mutexes, coordinates, direct ideas, war goals, claims, cores, AI strategies, unit spawns, and decision unlocks in all four audited focus files.
- `rg -n` broad scan of related scripted effects and ideas for helper-mediated idea/reward spam.
- `wc -l` on the four audited focus files plus related effects/ideas files.
- Python static parser for focus tree counts, focus counts, absolute coordinate estimation, direct `add_ideas` duplicates, long reward blocks, wide prerequisite spans, same-row/upward prerequisite risks, too-close coordinates, and mutual-exclusion span risks.
- Python helper-call extractor for repeated focus reward helpers and helper payload summaries.
- Python tag-focused extractor for `CFR`, `DSC`, `PRA`, `MFR`, `NRF`, `FEV`, and `OGB`.
- `git status --short`

Validation limitations:

- Static coordinate parsing estimates absolute coordinates from `x`, `y`, and `relative_position_id`; it does not render the focus tree.
- No in-game load was performed.
- No gfx, flags, sprites, or localisation files were touched.
- No fallback implementation or simplification was made.

