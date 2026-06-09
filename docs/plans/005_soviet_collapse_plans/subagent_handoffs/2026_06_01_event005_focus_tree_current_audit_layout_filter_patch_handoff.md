# Event005 Soviet Collapse Focus Tree Current Audit, Layout and Filter Patch Handoff

## Scope

Audit date: 2026-06-01.

User constraints followed:

- Did not edit `gfx/flags/`.
- Did not edit `interface/flags/`.
- Treated the dirty worktree as parent/user-owned and did not revert unrelated changes.
- Patch scope stayed inside `common/national_focus/005_soviet_collapse_*.txt` plus this handoff.

Required references read before focus-file inspection:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs/examples: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, plus vanilla `common/national_focus/generic.txt` and `common/national_focus/soviet.txt`
- Event source spec: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`

## Files Inspected

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` for exact helper behavior of `soviet_collapse_update_pra_authority_idea`
- `common/ideas/005_soviet_collapse_ideas.txt` for PRA authority idea lifecycle
- `localisation/english/*005_soviet_collapse*.yml` for focus name/description coverage

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_01_event005_focus_tree_current_audit_layout_filter_patch_handoff.md`

No localisation keys, icon ids, gfx files, flag files, scripted effects, scripted triggers, ideas, decisions, or interface files were changed.

## Patches Made

| Focus id | File | Before | After | Reason |
| --- | --- | --- | --- | --- |
| `PRA_switchyard_denial_posts` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:1491` | `x = 12`, `y = 5`; prerequisite line from `PRA_omsk_station_guard` ran through `PRA_repair_crews_without_ministries`. | `x = 13`, `y = 5`. | Bounded layout fix; preserves route logic and reward. |
| `blr_soviet_collapse_minsk_central_dispatch` | `common/national_focus/005_soviet_collapse_republics.txt:9840` | One grid unit from `blr_soviet_collapse_council_bargains_with_forests` on the same row. | `x = 8`, `y = 7`. | Bounded spacing fix; no prerequisite, reward, or route change. |
| `BBH_borderless_column_schools` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:8659` | Had `FOCUS_FILTER_RESEARCH` but no direct research/doctrine reward. | Added one-use land doctrine discount `BBH_borderless_column_schools_bonus`. | Filter now matches visible reward. |
| `UDC_front_dispatch_school` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:10360` | Had `FOCUS_FILTER_RESEARCH` but no direct research/doctrine reward. | Added one-use land doctrine discount `UDC_front_dispatch_school_bonus`. | Filter now matches visible reward. |
| `SDZ_informant_cipher_schools` | `common/national_focus/005_soviet_collapse_custom_splinters.txt:11554` | Had `FOCUS_FILTER_RESEARCH` but no direct research/doctrine reward. | Added one-use land doctrine discount `SDZ_informant_cipher_schools_bonus`. | Filter now matches visible reward. |

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Major republic political, industrial, military, diplomacy, expansion, League, and special-mechanic branches | `soviet_collapse_ukraine_focus_tree` in `005_soviet_collapse_republics.txt` with 83 focuses | Partial | Broad route surface exists, but pathline scanner still found several long diagonal crossings such as `ukr_soviet_collapse_british_caution -> ukr_soviet_collapse_officer_patronage_lists` near foreign/political nodes. Political routes still lean on helper rewards rather than frequent leader/advisor/law/cosmetic consequences. |
| Generic breakaway tree that is more than a fallback | `soviet_collapse_breakaway_focus_tree` with 36 focuses | Partial | Much deeper than older four-focus state, but still shared and helper-heavy. Needs country-specific adaptation or explicit fallback documentation for long-lived breakaways. |
| Internal republic compact | `soviet_collapse_internal_republic_focus_tree` with 62 focuses | Partial | Has regional paths and depth, but still needs more visible country adaptation and postwar settlement hooks. |
| Baltic, Caucasus, Central Asia, Moldova, Belarus regional republic branches | Regional trees with 40-53 focuses each | Partial | Route families exist. Remaining problems are layout congestion, shared-helper rewards, and limited postwar settlement/integration consequences. |
| Kazakhstan major successor | `soviet_collapse_kazakhstan_focus_tree` with 92 focuses | Partial/stronger | Strongest regional tree by count and route spread. Still has several long pathline risks around Alash, federation, resource, and southern republic branches. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` ancient trees, 16 focuses each | Partial/shallow | Political, industry, and expansion hooks exist, but 16-focus trees remain shallow for playable restored identities and still reuse the ancient icon family heavily. |
| Factory successors | `CFR` 47 focuses, `OGB` 23 focuses, `MFR` 58 focuses | Mixed | `CFR` and `MFR` have stronger industrial identity. `OGB_soviet_collapse_focus_tree` remains the shallowest factory successor and needs broader Volga/Idel-Ural/postwar integration depth. |
| High-chaos custom splinters should be dangerous/OP | `FTH`, `PRA`, compact `TSC/RMC/DSC/NRF/ICD`, and 47-focus splinters in `005_soviet_collapse_custom_splinters.txt` | Partial | Aggressive endpoints exist, e.g. `FTH_communes_without_capitals`, `PRA_rails_over_capitals`, `TSC_sky_over_siberia`, `RMC_procession_columns`, `DSC_dead_regiment_columns`, `NRF_icebound_marine_guard`, `ICD_grave_columns_march`, but compact 18-focus chaos countries still need stronger OP map pressure, war escalation, units, or collapse-mechanic damage. |

## Missing or Simplified Content

High priority:

1. `soviet_collapse_update_pra_authority_idea` is still called by 14 PRA focuses in `005_soviet_collapse_custom_splinters.txt`: `PRA_the_timetable_declares_authority`, `PRA_novosibirsk_dispatcher_court`, `PRA_omsk_station_guard`, `PRA_timetable_law`, `PRA_ticket_courts_for_every_platform`, `PRA_the_board_overrules_ministers`, `PRA_armored_train_directorate`, `PRA_passport_of_the_moving_state`, `PRA_neutral_corridor_letters`, `PRA_charge_for_safe_passage`, `PRA_league_transit_bargain`, `PRA_rails_over_capitals`, `PRA_flags_on_every_station`, and `PRA_the_pale_line_endures`. The helper is hidden and mostly idempotent, but it still repeatedly evaluates add/remove idea lifecycle logic. A broader scripted-system pass should consider a single route-state updater, not another focus-side patch.
2. Compact high-chaos trees remain underpowered relative to the event promise. `TSC_sky_over_siberia`, `RMC_procession_columns`, `DSC_dead_regiment_columns`, `NRF_icebound_marine_guard`, and `ICD_grave_columns_march` should become scarier through direct map pressure, special units, stronger war plans, collapse pressure, or hostile AI strategy. This is too broad for this subagent patch.
3. `OGB_soviet_collapse_focus_tree` is still only 23 focuses. It has Volga claims, Idel-Ural hooks, and a restoration state path, but lacks the same depth as `CFR` and `MFR`.
4. The 16-focus ancient restoration trees (`KZR`, `SOG`, `KHW`, `ALN`) cover basic identity but not enough internal politics, industry, and postwar handling for long-lived playable identities.

Secondary:

5. Several full custom splinters still use the 47-focus template architecture. They are much improved by route-specific names and reward hooks, but repeated branch rhythm remains visible around `*_birth`, `*_first_guard`, `*_stores`, `*_legitimacy`, `*_rival`, `*_economy`, `*_league`, `*_foreign`, `*_supply`, `*_war_plan`, and `*_endgame`.
6. Many focuses with industry/manpower filters rely on hidden identity helpers and generic custom tooltips rather than visible direct construction/unit/research rewards. This is often intentional, but it makes filter audits noisy and should be reviewed branch-by-branch before any broad changes.

## Icon Coverage Table

| Check | Result | Notes |
| --- | --- | --- |
| Focus blocks scanned | 1,698 | Across all four Event005 focus files. |
| Missing `icon =` assignment | 0 | Every focus has an icon assignment. |
| Unique icon ids | 1,498 | 200 repeated assignments beyond the first use. |
| Highest repeat count | 4 | Reused families include ancient restoration icons, `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_central_asia_soviet_collapse_steppe_federation`, and `GFX_moldova_soviet_collapse_ukrainian_corridor`. |
| Icon gfx definitions | Not patched | I did not edit gfx/interface assets. The user explicitly said flags are correct and must not be touched. |

## Localisation and Reward Mismatch List

| Check | Result | Notes |
| --- | --- | --- |
| Missing focus title/description keys in scanned `*005_soviet_collapse*.yml` files | 0 | Focus IDs and `_desc` keys are covered. |
| Localisation changed | 0 keys | No new on-screen text was added. Doctrine bonus names use internal bonus ids only. |
| Direct focus reward idea operations | 7 | All found direct `remove_ideas` operations are inside `hidden_effect`: `PRA_the_board_overrules_ministers`, `TSC_the_committee_of_instruments`, `RMC_communes_of_witnesses`, `DSC_witness_officers`, `NRF_living_harbor_committees`, `ICD_commissars_of_last_addresses`, `OGB_the_council_takes_the_seal`. No visible idea-removal spam was patched. |
| Research filter mismatches patched | 3 | `BBH_borderless_column_schools`, `UDC_front_dispatch_school`, and `SDZ_informant_cipher_schools` now have one-use land doctrine discounts. |

## AI Behavior Gaps

- Mechanical scan found `ai_will_do` present on all 1,698 focus blocks.
- Many AI blocks are still shallow `base =` weights or simple war/chaos modifiers. The biggest remaining design gap is not missing AI blocks; it is lack of route-aware strategic behavior for many major paths.
- High-chaos/extreme routes need stronger AI push when chaos tier is high, when SOV authority is low, or when the country is already at war with SOV. Examples needing deeper AI review: `TSC_sky_over_siberia`, `RMC_procession_columns`, `DSC_dead_regiment_columns`, `NRF_icebound_marine_guard`, `ICD_grave_columns_march`, `PRA_rails_over_capitals`, `KRS_every_harbor_a_soviet`.
- Regional republic diplomacy and League branches should more consistently weight foreign/League routes based on actual faction membership, neighboring breakaways, SOV threat values, war state, and sponsor appetite.

## Layout Findings

Patched:

- `PRA_omsk_station_guard -> PRA_switchyard_denial_posts` no longer runs through `PRA_repair_crews_without_ministries` after moving `PRA_switchyard_denial_posts` to `x = 13`, `y = 5`.
- `blr_soviet_collapse_minsk_central_dispatch` is no longer one grid unit from `blr_soviet_collapse_council_bargains_with_forests` after moving to `x = 8`, `y = 7`.

Remaining broad layout risks:

- Mechanical line-near-node scan still reports 74 possible pathline risks. These need visual review because many are acceptable long diagonals in large trees, but several are likely real readability problems.
- Representative remaining risks:
  - `UWD_propaganda -> UWD_settlement` near `UWD_rail_yard_repair_trust` in `005_soviet_collapse_custom_splinters.txt`.
  - `UWD_workers_canteen_compact -> UWD_kama_foundry_contracts` near `UWD_radical_turn`.
  - `BAC_war_plan -> BAC_militia_training_yards` near `BAC_industry_plan`.
  - `NLC_station_mediation -> NLC_winter_guarantees` near `NLC_settlement`.
  - Multiple Ukraine, Belarus, Moldova, Caucasus, and Kazakhstan long diagonals remain in `005_soviet_collapse_republics.txt`.
- Post-patch mechanical scan reports 0 duplicate focus IDs, 0 exact coordinate overlaps, and 0 very-close same-row pairs under the strict `dx < 2`, `dy < 1` check.

## Validation Run

Commands run:

```text
python3 brace balance check over common/national_focus/005_soviet_collapse_*.txt
python3 focus parser for duplicate ids, focus counts, icons, ai_will_do, completion_reward, search_filters, localisation coverage
python3 layout scanner for exact overlaps, very-close same-row pairs, and line-near-node risks
rg -n "soviet_collapse_update_pra_authority_idea = yes" common/national_focus/005_soviet_collapse_custom_splinters.txt
nl -ba common/national_focus/005_soviet_collapse_custom_splinters.txt
nl -ba common/national_focus/005_soviet_collapse_republics.txt
```

Results:

- Brace balance: 0 imbalance and 0 negative-close events in all four Event005 focus files.
- Duplicate focus IDs: 0.
- Exact coordinate overlaps: 0.
- Very-close same-row pairs: 0 after patch.
- Missing `ai_will_do`: 0.
- Missing `completion_reward`: 0.
- Empty/missing `search_filters`: 0.
- Missing focus title/description localisation: 0.
- Confirmed doctrine bonuses now present on `BBH_borderless_column_schools`, `UDC_front_dispatch_school`, and `SDZ_informant_cipher_schools`.

Skipped validation:

- Did not run the game or inspect live focus-tree rendering.
- Did not validate gfx sprite definitions or DDS files.
- Did not edit or inspect `gfx/flags` or `interface/flags`.

## Remaining Route Risks for Parent

- PRA authority idea churn should be solved at scripted-system/route-state level if the parent wants fewer repeated add/remove evaluations. The exact helper is `soviet_collapse_update_pra_authority_idea` in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- High-chaos compact trees are still not consistently dangerous enough for the event promise. They need broader design work, not more small rewards.
- OGB and ancient restoration trees need expansion plans if they are expected to stand beside the larger successor trees.
- Many 47-focus custom splinter trees still share recognizable branch skeletons. A parent pass should choose which ones need unique endgame mechanics versus which are acceptable as standard splinter packages.

No separate improvement plan was written in this pass; the remaining gaps are already suitable parent implementation targets and exceed the allowed small-patch scope.
