# Event005 Soviet Collapse Focus Tree Full Depth/Layout Audit

Date: 2026-06-01
Scope: current-state audit of all `005_soviet_collapse` national focus files.
Mode: focus-tree analysis only. No gameplay files, flag files, flag sprites, or interface flag files were edited.

## Source Rules And References Consulted

Required project instructions and skills read:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Offline Paradox wiki pages consulted before inspecting/editing focus files:

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
- `paradox_wiki/AI focuses - Hearts of Iron 4 Wiki.md`

Vanilla documentation/examples consulted:

- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`
- `~/projects/Hearts of Iron IV/common/ai_strategy/_documentation.md`
- `~/projects/Hearts of Iron IV/common/focus_inlay_windows/documentation.md`
- Vanilla focus precedents from `common/national_focus/generic.txt`, `common/national_focus/finland.txt`, and `common/national_focus/spain.txt`

Event005 design references consulted:

- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `docs/events/005_soviet_collapse.md`

Key syntax/layout checks applied from references:

- Focus IDs must be unique across loaded focus content.
- `relative_position_id` must not create invalid chains/cycles.
- Multiple focuses inside one `prerequisite = { ... }` are OR prerequisites; separate `prerequisite` blocks are AND prerequisites.
- Parent focuses should visually precede children; same-row or reversed dependency chains are layout risks.
- Mutually exclusive focuses on the same row can create visible line collisions when unrelated focuses sit between them.
- Focus filters should correspond to visible rewards.

## Files In Scope

The audit found four current Soviet Collapse focus files:

| File | Lines | Focus trees | Focus ids |
|---|---:|---:|---:|
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 1,523 | 4 | 64 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25,408 | 25 | 1,005 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3,069 | 3 | 128 |
| `common/national_focus/005_soviet_collapse_republics.txt` | 12,031 | 9 | 501 |
| Total | 42,031 | 41 | 1,698 |

No duplicate focus IDs were detected among the 1,698 focus blocks.

## Focus Tree Counts

| File | Tree id | Start line | Focus count |
|---|---|---:|---:|
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | 13 | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | 395 | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | 778 | 16 |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_soviet_collapse_ancient_focus_tree` | 1164 | 16 |
| `005_soviet_collapse_custom_splinters.txt` | `FTH_soviet_collapse_focus_tree` | 15 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `PRA_soviet_collapse_focus_tree` | 1201 | 22 |
| `005_soviet_collapse_custom_splinters.txt` | `TSC_soviet_collapse_focus_tree` | 1787 | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `RMC_soviet_collapse_focus_tree` | 2254 | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `DSC_soviet_collapse_focus_tree` | 2728 | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `NRF_soviet_collapse_focus_tree` | 3300 | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `ICD_soviet_collapse_focus_tree` | 3797 | 18 |
| `005_soviet_collapse_custom_splinters.txt` | `BSC_soviet_collapse_focus_tree` | 4262 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `TNC_soviet_collapse_focus_tree` | 5381 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ALA_soviet_collapse_focus_tree` | 6510 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BBH_soviet_collapse_focus_tree` | 7619 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KRS_soviet_collapse_focus_tree` | 8808 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UDC_soviet_collapse_focus_tree` | 10034 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SDZ_soviet_collapse_focus_tree` | 11218 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `GAC_soviet_collapse_focus_tree` | 12452 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_soviet_collapse_focus_tree` | 13622 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_soviet_collapse_focus_tree` | 14821 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `FEV_soviet_collapse_focus_tree` | 16010 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `SZA_soviet_collapse_focus_tree` | 17173 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `UWD_soviet_collapse_focus_tree` | 18338 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `MRC_soviet_collapse_focus_tree` | 19525 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `IUL_soviet_collapse_focus_tree` | 20698 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `BAC_soviet_collapse_focus_tree` | 21840 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `ARD_soviet_collapse_focus_tree` | 22975 | 47 |
| `005_soviet_collapse_custom_splinters.txt` | `NLC_soviet_collapse_focus_tree` | 24176 | 47 |
| `005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 16 | 47 |
| `005_soviet_collapse_factory_successors.txt` | `OGB_soviet_collapse_focus_tree` | 1140 | 23 |
| `005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 1746 | 58 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 18 | 83 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 2326 | 36 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 3117 | 62 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 4583 | 42 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 5541 | 40 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 6446 | 45 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 7566 | 48 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 8710 | 53 |
| `005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 10013 | 92 |

## Route Coverage Table

| Required route/content family | Implemented coverage | Audit status |
|---|---|---|
| Major republic and regional successor routes | 9 trees in `005_soviet_collapse_republics.txt`, including Ukraine, breakaway, internal republics, Baltic, Caucasus, Central Asia, Moldova, Belarus, and Kazakhstan. | Partially covered. Political, industrial, and military branches exist, but several trees have sparse direct decision, war, faction, map, or evolution hooks. Layout issues are concentrated in Baltic, Moldova, Belarus, and breakaway shared trees. |
| Custom splinter countries | 25 trees in `005_soviet_collapse_custom_splinters.txt`. Most are 47-focus full trees; `PRA` has 22 focuses; `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` have 18-focus compact trees. | Broadly present but uneven. The 18-focus trees are shallow for high-chaos states. The 47-focus trees frequently repeat generic helper patterns, flags, stats, and variables, with fewer visible special mechanics than the spec implies. |
| Ancient restorations | 4 trees in `005_soviet_collapse_ancient_restorations.txt`: KZR, SOG, KHW, ALN. | Present but shallow. Each is 16 focuses and has a similar compact structure. They have old-name and annexation/recovery identity beats, but weak decision/diplomacy/special-mechanic depth and repeated icon families. |
| Factory and industrial successor states | 3 trees in `005_soviet_collapse_factory_successors.txt`: CFR, OGB, MFR. | Present. CFR and MFR are substantial; OGB is compact. Direct decision and war hooks exist in the file, but first-row industrial/political filters sometimes do not match visible rewards, and OGB remains shallow. |
| High-chaos overpowered/aggressive successor behavior | Helpers such as `soviet_collapse_apply_focus_chaos_assault_plan`, `soviet_collapse_apply_custom_splinter_expansion_claims`, and `soviet_collapse_spawn_custom_splinter_assault_columns` are used in several routes. | Needs targeted follow-up. The aggressive hooks are helper-mediated and not consistently visible from individual focus reward text/filter structure. Several high-chaos end focuses still look like flags/helpers rather than obvious claim/core/war/assault payoffs. |
| Decision, release, aggression, influence, evolution, faction, scenario, core/claim, and unit integration | Some direct decision, event, faction, map, unit, AI-strategy, and war-goal markers exist, with many more likely hidden through scripted helpers. | Uneven. The audit found 128 focus blocks with no direct marker for decisions, map effects, war/faction hooks, events, identity changes, buildings, units, or AI strategy. These may be helper-backed, but they are high-value manual review targets because reward visibility and route identity can feel disconnected. |

## Idea Spam Risk

Direct focus reward scan:

- Direct `add_ideas` / `add_timed_idea` in focus rewards: 0.
- Focuses granting the same direct idea multiple times: none found.

Helper-mediated idea risk:

- 14 `PRA` focuses call `soviet_collapse_update_pra_authority_idea`.
- The helper is defined at `common/scripted_effects/005_soviet_collapse_effects.txt:7432` and can add one of:
  - `pra_moving_state_authority`
  - `pra_corridor_toll_authority`
  - `pra_railway_guard`
  - `pra_timetable_sovereignty_board`

Concrete PRA focus callers:

| Focus id | Line | Risk |
|---|---:|---|
| `PRA_the_timetable_declares_authority` | `005_soviet_collapse_custom_splinters.txt:1208` | Authority idea lifecycle helper called. |
| `PRA_novosibirsk_dispatcher_court` | `005_soviet_collapse_custom_splinters.txt:1229` | Authority idea lifecycle helper called. |
| `PRA_omsk_station_guard` | `005_soviet_collapse_custom_splinters.txt:1252` | Authority idea lifecycle helper called. |
| `PRA_timetable_law` | `005_soviet_collapse_custom_splinters.txt:1308` | Authority idea lifecycle helper called. |
| `PRA_ticket_courts_for_every_platform` | `005_soviet_collapse_custom_splinters.txt:1331` | Authority idea lifecycle helper called. |
| `PRA_the_board_overrules_ministers` | `005_soviet_collapse_custom_splinters.txt:1354` | Authority idea lifecycle helper called. |
| `PRA_armored_train_directorate` | `005_soviet_collapse_custom_splinters.txt:1379` | Authority idea lifecycle helper called. |
| `PRA_passport_of_the_moving_state` | `005_soviet_collapse_custom_splinters.txt:1539` | Authority idea lifecycle helper called. |
| `PRA_neutral_corridor_letters` | `005_soviet_collapse_custom_splinters.txt:1562` | Authority idea lifecycle helper called. |
| `PRA_charge_for_safe_passage` | `005_soviet_collapse_custom_splinters.txt:1583` | Authority idea lifecycle helper called. |
| `PRA_league_transit_bargain` | `005_soviet_collapse_custom_splinters.txt:1607` | Authority idea lifecycle helper called. |
| `PRA_rails_over_capitals` | `005_soviet_collapse_custom_splinters.txt:1683` | Authority idea lifecycle helper called. |
| `PRA_flags_on_every_station` | `005_soviet_collapse_custom_splinters.txt:1725` | Authority idea lifecycle helper called. |
| `PRA_the_pale_line_endures` | `005_soviet_collapse_custom_splinters.txt:1754` | Authority idea lifecycle helper called. |

This looks like an intended staged-authority design, not direct idea spam. It is still a review risk because repeated focus calls into a direct idea-adder can stack stale ideas if cleanup or swap exclusivity is incomplete.

Other idea helpers found in `005_soviet_collapse_effects.txt` are mostly setup or decision/system effects, not direct focus reward spam. Examples include republican setup, CFR construction mandates, MFR arsenal quotas, and ancient restoration setup ideas.

## Repeated Helper Reward Risk

The focus trees use repeated scripted helpers heavily. This is good for consistency, but it also makes several routes feel generic when the focus reward has only flags, variables, stats, or a common helper call.

Top helper calls found in focus rewards:

| Helper | Focus calls | Risk |
|---|---:|---|
| `soviet_collapse_apply_focus_depot_and_supply_control` | 138 | Repeated military/supply reward pattern across many countries. |
| `soviet_collapse_apply_focus_military_consolidation` | 132 | Repeated army consolidation pattern. |
| `soviet_collapse_apply_focus_legal_recognition` | 117 | Repeated political recognition pattern. |
| `soviet_collapse_apply_focus_republican_compact_plan` | 80 | Repeated state-building pattern. |
| `soviet_collapse_apply_objective_source_pressure_delta` | 63 | Repeated pressure-variable reward without always-visible gameplay hook. |
| `soviet_collapse_apply_focus_foreign_channel` | 63 | Repeated diplomacy helper, often with weak direct diplomacy/faction follow-through. |
| `soviet_collapse_apply_focus_high_chaos_identity` | 60 | Repeated identity helper across high-chaos splinters. |
| `soviet_collapse_apply_focus_security_supply_plan` | 57 | Repeated security/supply reward pattern. |
| `soviet_collapse_apply_focus_league_preparation` | 52 | Repeated league-preparation reward pattern. |

Follow-up should focus on visible reward variety and payoff clarity, not deleting helper usage.

## Shallow Or Simplified Route Content

High-priority shallow areas:

- `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree` are 18 focuses each. These are compact for high-chaos splinters and need stronger special mechanics, expansion, diplomacy, and aggressive payoff visibility.
- All four ancient restoration trees are 16 focuses each. They read as compact symbolic restorations instead of deep successor-state gameplay. They need more decision/mechanic hooks if they are expected to rival full successor states.
- `OGB_soviet_collapse_focus_tree` is 23 focuses and has less depth than CFR/MFR. Its early political/religious/scholarly identity focuses are mostly setup/stat/variable driven.
- Several republic/regional trees have political, industry, and military coverage but lack direct decision, war, faction, claim/core, scenario, or evolution markers in the scanned focus rewards. These may be hidden by helpers, but the focus reward surface is weak.
- Many high-chaos custom splinter trees are 47 focuses but still repeat the same route skeleton: birth focus, consolidation, mediation/settlement, radical turn, supplies, military, foreign channel, league preparation, endpoint. They need more country-specific mechanics and more obvious aggression if the design goal is overpowered chaos states.

Concrete disconnected reward candidates found by scanner include:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:129` `KZR_caspian_patrol_letters`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:497` `SOG_scholar_envoy_rooms`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:31` `FTH_birth`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:410` `FTH_radical_turn`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1815` `TSC_tura_observation_presidium`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1932` `TSC_the_committee_of_instruments`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1961` `TSC_the_committee_of_signs`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2144` `TSC_sky_over_siberia`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2282` `RMC_tambov_witness_cells`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2611` `RMC_procession_columns`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3825` `ICD_ryazan_grave_commissariat`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:4148` `ICD_grave_columns_march`

These should be manually checked before patching because helper calls may provide hidden behavior; the issue is that the current focus surface does not clearly expose distinctive systems.

## Layout Risk Findings

The layout scanner found 35 risks. Most are mutually exclusive same-row choices with another focus sitting between the pair. These can cause overlapping or visually confusing focus path lines.

High-confidence examples:

| Tree/section | File/line references | Risk |
|---|---|---|
| `soviet_collapse_baltic_focus_tree` political fork | `005_soviet_collapse_republics.txt:4706`, `:4741`, `:4776`, `:4807`, with `:5353` between several same-row pairs | Four same-row route choices and a later focus share the route row; mutual exclusion/path lines are likely to cross or overlap. |
| `soviet_collapse_moldova_focus_tree` union fork | `005_soviet_collapse_republics.txt:7927`, `:7960`, `:7992`, with `:8542` and `:8569` between | Three mutually exclusive union positions are on one row with unrelated recovery/border focuses between them. |
| `soviet_collapse_belarus_focus_tree` route row | `005_soviet_collapse_republics.txt:8879`, `:8910`, `:8943`, `:8975` | Same-row mutually exclusive route choices are widely spaced and likely create long crossing lines; scanner also found one same-row proximity issue in the tree. |
| `soviet_collapse_breakaway_focus_tree` route row | `005_soviet_collapse_republics.txt:2461`, `:2497`, `:2527`, `:2565` | Same-row route choices have an unrelated/bridging focus between mutual exclusion pairs. |
| `UDC_soviet_collapse_focus_tree` settlement fork | `005_soviet_collapse_custom_splinters.txt:10727`, `:11008`, `:11044` | `UDC_loyalist_statute_guarantees` sits between `UDC_settlement` and `UDC_radical_turn` on the same row. |
| `SDZ_soviet_collapse_focus_tree` settlement fork | `005_soviet_collapse_custom_splinters.txt:11937`, `:12237`, `:12273` | `SDZ_chain_of_custody_statutes` sits between `SDZ_settlement` and `SDZ_radical_turn` on the same row. |
| `GAC_soviet_collapse_focus_tree` settlement fork | `005_soviet_collapse_custom_splinters.txt:13372`, `:13420`, `:13456` | `GAC_harvest_truce_guarantees` sits between `GAC_settlement` and `GAC_radical_turn` on the same row. |
| `DHC_soviet_collapse_focus_tree` settlement fork | `005_soviet_collapse_custom_splinters.txt:14411`, `:14534`, `:14570` | `DHC_convoy_autonomy_guarantees` sits between `DHC_settlement` and `DHC_radical_turn` on the same row. |
| `KHC_soviet_collapse_focus_tree` settlement fork | `005_soviet_collapse_custom_splinters.txt:15604`, `:15725`, `:15761` | `KHC_grain_passage_guarantees` sits between `KHC_settlement` and `KHC_radical_turn` on the same row. |

Suspicious relative-position patterns:

- No duplicate focus IDs and no brace imbalance were found.
- No obvious `relative_position_id` cycle was reported by the scanner.
- The main layout risk is not syntax failure; it is same-row spacing and crossing mutual exclusion/path lines.

## Icon Coverage

| Check | Result |
|---|---:|
| Focuses missing an icon assignment | 0 |
| Missing localisation for focus title/description keys | 0 |
| Reused focus icon IDs | 140 duplicated icon IDs |

Examples of repeated icon families:

| Icon id | Reuse examples | Risk |
|---|---|---|
| `GFX_focus_soviet_collapse_ancient_workshop_compact` and related ancient icon family | Reused across KZR/SOG/KHW/ALN, including lines `84`, `466`, `849`, `1235` and analogous branch icons | Ancient restoration trees visually blend together despite distinct identity promises. |
| `GFX_focus_FEV_diplomatic_plan` | `005_soviet_collapse_custom_splinters.txt:16689`, `:16823`, `:16902`, `:17102` | Repeated diplomacy icon inside one tree. |
| `GFX_focus_SZA_diplomatic_plan` | `005_soviet_collapse_custom_splinters.txt:17840`, `:17969`, `:18048`, `:18267` | Repeated diplomacy icon inside one tree. |
| `GFX_focus_MRC_civil_rule` | `005_soviet_collapse_custom_splinters.txt:19753`, `:19901`, `:20003`, `:20235` | Repeated civil rule icon inside one tree. |
| `GFX_focus_MRC_foreign` | `005_soviet_collapse_custom_splinters.txt:19822`, `:19845`, `:20461`, `:20510` | Repeated foreign-policy icon inside one tree. |
| `GFX_focus_IUL_supply` | `005_soviet_collapse_custom_splinters.txt:20951`, `:21150`, `:21463`, `:21669` | Repeated supply icon inside one tree. |
| `GFX_focus_IUL_war_plan` | `005_soviet_collapse_custom_splinters.txt:21261`, `:21394`, `:21587`, `:21701` | Repeated war-plan icon inside one tree. |
| `GFX_focus_soviet_collapse_guard_the_radio_stations` | `005_soviet_collapse_republics.txt:54`, `:2356`, `:2769`, `:3160` | Shared generic opening icon across multiple republic/shared trees. |
| `GFX_ukr_soviet_collapse_democratic` | `005_soviet_collapse_republics.txt:313`, `:819`, `:950`, `:971` | Repeated Ukraine democratic icon across different route beats. |
| `GFX_moldova_soviet_collapse_ukrainian_corridor` | `005_soviet_collapse_republics.txt:7750`, `:7886`, `:8202`, `:8226` | Repeated Moldova corridor icon across multiple focuses. |

No asset or flag files were touched. The icon findings are script/reference findings only.

## Localisation And Reward Mismatch Findings

Localisation:

- Missing focus title keys: 0 found.
- Missing focus description keys: 0 found.
- Localisation files were inspected only as data sources; no localisation edits were made.

Reward/filter mismatch examples:

| Focus id | File/line | Filter | Finding |
|---|---|---|---|
| `CFR_count_the_cranes` | `005_soviet_collapse_factory_successors.txt:32` | `FOCUS_FILTER_INDUSTRY` | Direct reward surface has no visible building/stockpile/research payload; likely helper-backed, but the filter does not visibly match the reward. |
| `MFR_orders_outlive_ministries` | `005_soviet_collapse_factory_successors.txt:1762` | `FOCUS_FILTER_INDUSTRY` | Direct reward surface is flag/helper driven and not visibly industrial. |
| `BSC_supply` | `005_soviet_collapse_custom_splinters.txt:4582` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `BSC_hidden_road_depots` | `005_soviet_collapse_custom_splinters.txt:4831` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `BSC_industry_plan` | `005_soviet_collapse_custom_splinters.txt:5260` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `TNC_stores` | `005_soviet_collapse_custom_splinters.txt:5442` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `TNC_economy` | `005_soviet_collapse_custom_splinters.txt:5530` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `TNC_supply` | `005_soviet_collapse_custom_splinters.txt:5695` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `TNC_railway_officer_schools` | `005_soviet_collapse_custom_splinters.txt:5665` | `FOCUS_FILTER_RESEARCH` | Research filter without a visible direct research payload. |
| `ALA_alash_officer_schools` | `005_soviet_collapse_custom_splinters.txt:6796` | `FOCUS_FILTER_RESEARCH` | Research filter without a visible direct research payload. |
| `ALA_steppe_communications_congress` | `005_soviet_collapse_custom_splinters.txt:6963` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |
| `ALA_tashkent_contact_rooms` | `005_soviet_collapse_custom_splinters.txt:7118` | `FOCUS_FILTER_INDUSTRY` | Industry filter without a visible direct industry payload. |

These findings do not prove no reward exists because many rewards are helper-mediated. They do identify focuses where the filter/player expectation should be manually compared against the helper effect and tooltip.

## AI Behavior Gaps

Scanner result:

- All 1,698 focus blocks have an `ai_will_do` block.

Remaining AI risks:

- Presence of `ai_will_do` is not the same as route-aware AI. Many trees appear to use broad weights rather than strong route locks or state-aware strategy shifts.
- Direct `add_ai_strategy` markers are sparse and concentrated in specific trees. Several republic/regional trees do not visibly set AI strategy from focus rewards.
- Mutually exclusive route rows need audit for AI route consistency. If weights do not lock a country into a coherent political branch, AI can wander between shallow generic payoffs.
- High-chaos splinters should be aggressive/overpowered by design, but their focus reward surface often relies on common helpers instead of visible war/claim/unit behavior. AI aggression should be rechecked against the helper effects and scripted AI strategy.

## High-Priority Fix List: Worst 20 Focus IDs Or Sections

1. `soviet_collapse_baltic_focus_tree` political fork: `baltic_soviet_collapse_legal_continuity_government` (`005_soviet_collapse_republics.txt:4706`), `baltic_soviet_collapse_military_border_government` (`:4741`), `baltic_soviet_collapse_baltic_league_first` (`:4776`), `baltic_soviet_collapse_foreign_protection_council` (`:4807`), and `baltic_soviet_collapse_singing_barricades_early` (`:5353`). Patch first for same-row mutual exclusion/pathline clutter.
2. `soviet_collapse_moldova_focus_tree` union fork: `moldova_soviet_collapse_alliance_not_union` (`005_soviet_collapse_republics.txt:7927`), `moldova_soviet_collapse_conditional_union` (`:7960`), `moldova_soviet_collapse_reject_the_union_question` (`:7992`), with `moldova_soviet_collapse_black_soil_recovery_boards` (`:8542`) and `moldova_soviet_collapse_smugglers_and_border_committees` (`:8569`) between same-row choices.
3. `soviet_collapse_belarus_focus_tree` identity row: `blr_soviet_collapse_national_council_of_minsk` (`005_soviet_collapse_republics.txt:8879`), `blr_soviet_collapse_socialist_autonomy_without_moscow` (`:8910`), `blr_soviet_collapse_military_transit_directorate` (`:8943`), `blr_soviet_collapse_foreign_corridor_administration` (`:8975`). Patch route spacing/pathline clarity.
4. `soviet_collapse_breakaway_focus_tree` route row: `soviet_collapse_capital_committee_records` (`005_soviet_collapse_republics.txt:2461`), `soviet_collapse_socialist_sovereignty_committee` (`:2497`), `soviet_collapse_military_defense_council` (`:2527`), `soviet_collapse_foreign_liaison_government` (`:2565`). Patch same-row mutual exclusion line risk.
5. `UDC_settlement` (`005_soviet_collapse_custom_splinters.txt:11008`) and `UDC_radical_turn` (`:11044`) with `UDC_loyalist_statute_guarantees` (`:10727`) between them. Patch row/relative placement.
6. `SDZ_settlement` (`005_soviet_collapse_custom_splinters.txt:12237`) and `SDZ_radical_turn` (`:12273`) with `SDZ_chain_of_custody_statutes` (`:11937`) between them. Patch row/relative placement.
7. `GAC_settlement` (`005_soviet_collapse_custom_splinters.txt:13420`) and `GAC_radical_turn` (`:13456`) with `GAC_harvest_truce_guarantees` (`:13372`) between them. Patch row/relative placement.
8. `DHC_settlement` (`005_soviet_collapse_custom_splinters.txt:14534`) and `DHC_radical_turn` (`:14570`) with `DHC_convoy_autonomy_guarantees` (`:14411`) between them. Patch row/relative placement.
9. `KHC_settlement` (`005_soviet_collapse_custom_splinters.txt:15725`) and `KHC_radical_turn` (`:15761`) with `KHC_grain_passage_guarantees` (`:15604`) between them. Patch row/relative placement.
10. PRA authority chain: `PRA_the_timetable_declares_authority` (`005_soviet_collapse_custom_splinters.txt:1208`) through `PRA_the_pale_line_endures` (`:1754`) repeatedly call `soviet_collapse_update_pra_authority_idea` (`common/scripted_effects/005_soviet_collapse_effects.txt:7432`). Verify idea cleanup/swap exclusivity before adding more authority focus calls.
11. Ancient restoration repeated icon family: KZR/SOG/KHW/ALN analogous focuses such as `KZR_workshop_compact` (`005_soviet_collapse_ancient_restorations.txt:84`), `SOG_workshop_compact` (`:466`), `KHW_workshop_compact` (`:849`), and `ALN_workshop_compact` (`:1235`). Patch icon variety or accept documented shared icon reuse.
12. `CFR_count_the_cranes` (`005_soviet_collapse_factory_successors.txt:32`). Patch industry filter/reward visibility if helper does not provide a clear industry tooltip.
13. `MFR_orders_outlive_ministries` (`005_soviet_collapse_factory_successors.txt:1762`). Patch industry filter/reward visibility if helper does not provide a clear industry tooltip.
14. BSC industrial cluster: `BSC_supply` (`005_soviet_collapse_custom_splinters.txt:4582`), `BSC_hidden_road_depots` (`:4831`), and `BSC_industry_plan` (`:5260`). Patch industry filter mismatch and improve visible reward variety.
15. Research-filter mismatches: `TNC_railway_officer_schools` (`005_soviet_collapse_custom_splinters.txt:5665`) and `ALA_alash_officer_schools` (`:6796`). Add visible research payload or change filters after checking helper effects.
16. Generic birth/radical route entry pattern: `FTH_birth` (`005_soviet_collapse_custom_splinters.txt:31`) and `FTH_radical_turn` (`:410`) are representative. Many birth/radical focuses are flags/stats/variables only; first focuses should reveal a distinct system or decision hook.
17. TSC compact route depth: `TSC_tura_observation_presidium` (`005_soviet_collapse_custom_splinters.txt:1815`), `TSC_the_committee_of_instruments` (`:1932`), `TSC_the_committee_of_signs` (`:1961`), and `TSC_sky_over_siberia` (`:2144`). Patch special-mechanic/aggression visibility if helper review confirms shallow rewards.
18. High-chaos compact aggression endpoints: `RMC_procession_columns` (`005_soviet_collapse_custom_splinters.txt:2611`), `ICD_grave_columns_march` (`:4148`), and `TSC_sky_over_siberia` (`:2144`). Verify they are actually overpowered/aggressive enough through units/claims/war/assault effects.
19. OGB early legitimacy section: `OGB_restore_the_bolghar_name` (`005_soviet_collapse_factory_successors.txt:1175`), `OGB_scholars_guard_the_charter` (`:1218`), and `OGB_clerics_guard_the_charter` (`:1238`). Patch decision/identity/advisor visibility if helper review confirms mostly stat/variable rewards.
20. Regional republic end-state integration: `soviet_collapse_baltic_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_moldova_focus_tree`, and `soviet_collapse_kazakhstan_focus_tree` should be reviewed after layout fixes for direct faction/war/map/core/claim/evolution hooks. Scanner found limited direct markers compared with the route promises.

## Validation Commands Run

Commands were read-only except for writing this report.

```bash
find common/national_focus -maxdepth 1 -type f -iname '*005*soviet*collapse*.txt' -print
wc -l common/national_focus/005_soviet_collapse_*.txt
rg -n '^focus_tree\s*=\s*\{' common/national_focus/005_soviet_collapse_*.txt
rg -n 'add_ideas|add_timed_idea|swap_ideas|remove_ideas' common/national_focus/005_soviet_collapse_*.txt common/scripted_effects/005_soviet_collapse_effects.txt
rg -n 'relative_position_id|mutually_exclusive|prerequisite|ai_will_do|search_filters|completion_reward' common/national_focus/005_soviet_collapse_*.txt
rg -n '^(soviet_collapse|KZR_|SOG_|KHW_|ALN_|FTH_|PRA_|TSC_|RMC_|DSC_|NRF_|ICD_|BSC_|TNC_|ALA_|BBH_|KRS_|UDC_|SDZ_|GAC_|DHC_|KHC_|FEV_|SZA_|UWD_|MRC_|IUL_|BAC_|ARD_|NLC_|CFR_|OGB_|MFR_|baltic_|moldova_|blr_)' localisation/english/*005_soviet_collapse*.yml
python3 - <<'PY'
# Read-only parser used to extract focus_tree blocks, direct focus blocks, ids, x/y positions,
# icons, filters, ai_will_do, completion_reward content, mutual exclusions, prerequisites,
# helper calls, direct idea effects, duplicated icons, localisation coverage, and layout risks.
PY
python3 - <<'PY'
# Read-only brace balance check for all 005_soviet_collapse focus files.
PY
git status --short
```

Validation results:

- 4 focus files found.
- 41 focus trees found.
- 1,698 focus blocks found.
- Duplicate focus IDs: 0.
- Brace balance: balanced in all four focus files.
- Missing focus icons: 0.
- Missing focus title/description localisation keys in scanned Event005 localisation files: 0.
- Direct focus reward `add_ideas` / `add_timed_idea`: 0.
- Focus blocks missing `ai_will_do`: 0.
- Layout risks found: 35.
- Reused icon IDs found: 140 duplicated icon IDs.

Skipped checks:

- Did not run HOI4 or live game validation.
- Did not inspect game logs.
- Did not patch focus, gameplay, localisation, interface, or asset files.
- Did not touch `gfx/flags`, `interface/flags`, or any flag sprite/image files.

## Changed Files

- Added this audit report only:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_focus_tree_full_depth_layout_audit.md`

No focus IDs, localisation keys, icon IDs, gameplay files, or assets were changed.

## Remaining Route Risks

- Helper-mediated rewards need manual inspection before patching because scanner output can undercount effects hidden inside scripted helpers.
- The highest-confidence immediate patches are layout-only row/relative-position adjustments in Baltic, Moldova, Belarus, breakaway, UDC, SDZ, GAC, DHC, and KHC.
- The next safest pass is filter/reward alignment for focuses where the helper does not provide a visible industry or research effect.
- Broader depth work for compact 18-focus high-chaos trees and 16-focus ancient restoration trees should be planned before implementation; it is larger than a safe local syntax/layout patch.
