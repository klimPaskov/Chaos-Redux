# Event 005 Soviet Collapse Focus Tree Current Audit and PRA Layout/Filter Patch

Timestamp: 2026-05-31 17:21:46 UTC

Role: Chaos Redux focus tree subagent.

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Additional focus-localisation files matching `localisation/english/*005_soviet_collapse*_english.yml` for current localisation coverage.

Hard constraints respected:

- No `gfx/flags`, flags, sprites, interface assets, or image files were edited.
- No Ukraine focus ids were edited.
- No commit was made.
- The worktree was already dirty. `git diff` for the touched focus file includes prior parent/subagent changes outside this pass; this handoff only claims the two PRA focus edits listed below.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, `common/focus_inlay_windows/documentation.md`.
- Vanilla focus precedent: `common/national_focus/argentina.txt` for focus filters, `ai_will_do`, relative layout, and continuous focus positioning.
- Event 005 specs: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md` and part 6 country/splinter requirements.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Moved `PRA_repair_crews_without_ministries` from `x = 8` to `x = 10`; changed `PRA_claim_the_branch_lines` focus filter from political/army to industry. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_172146_event005_focus_tree_current_audit_pra_layout_filter_patch.md` | This handoff. |

Changed focus ids:

- `PRA_repair_crews_without_ministries` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1409`
- `PRA_claim_the_branch_lines` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:1642`

Localisation keys changed: none.

Icon ids changed: none.

Visual assets changed: none.

## Route Behavior Before and After

Before:

- `PRA_repair_crews_without_ministries` sat at `(8, 3)`.
- The likely focus pathlines from `PRA_omsk_station_guard` to both `PRA_armored_train_directorate` and `PRA_switchyard_denial_posts` passed through that coordinate, visually crossing an unrelated industry/logistics focus.
- `PRA_claim_the_branch_lines` used `FOCUS_FILTER_POLITICAL FOCUS_FILTER_ARMY_XP`, but its reward is rail/logistics work: `unlock_decision_tooltip = pra_drive_the_junction_columns`, rail/infrastructure construction, depot control, and `soviet_collapse_apply_focus_depot_and_supply_control = yes`.

After:

- `PRA_repair_crews_without_ministries` is at `(10, 3)`, clearing the two detected PRA pathline hits.
- `PRA_claim_the_branch_lines` uses `FOCUS_FILTER_INDUSTRY`, matching its rail/infrastructure/depot reward.
- No prerequisites, mutual exclusions, availability, reward effects, AI weights, icons, localisation, decisions, ideas, flags, claims, cores, war goals, or formable hooks changed.

## Route Coverage Table

| Required route/content area | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine major tree | `soviet_collapse_ukraine_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:19`, 83 focuses | Broad but layout-risky | Avoided by request. It has real route content but the scan still reports 41 likely pathline hits and repeated icon use. |
| Generic breakaway republics | `soviet_collapse_breakaway_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:2350`, 36 focuses | Simplified | Political/industry/defense/diplomacy route labels exist, but much of the payoff is helper-driven and several pathlines likely cross. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:3135`, 62 focuses | Partial | Compact branch variety exists for KAR/KOM/CRI/TAT/BSK/FER/YAK/BYA/TAN, but route mechanics are heavily helper-based and pathline risk remains. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:4601`, 42 focuses | Partial | Legal restoration, defense, ports, and foreign recognition exist; static scan shows 23 likely pathline hits and repeated icons. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:5547`, 40 focuses | Partial | Oil, mountain, diplomacy, and route fork content exists, but branch rewards still lean on shared helpers. |
| Central Asian republics | `soviet_collapse_central_asia_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:6452`, 45 focuses | Partial | Southern, Basmachi, federation, and old movement content exists; route identity is better than generic republics but still has helper-heavy rewards and pathline risk. |
| Moldova | `soviet_collapse_moldova_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:7572`, 48 focuses | Partial | Dniester, Romania/Ukraine, agrarian, and observer-route content exists, but 22 likely pathline hits remain. |
| Belarus | `soviet_collapse_belarus_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:8715`, 53 focuses | Partial | Rail/forest/corridor identity is visible, but it still has 25 likely pathline hits and repeated small rewards. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`, `common/national_focus/005_soviet_collapse_republics.txt:10033`, 92 focuses | Broad but cramped | Strong route surface by count, but the tree spans 35 columns and still has 45 likely pathline hits. No edit made. |
| Full custom splinters | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` trees in `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Present but template-heavy | Most have 47 focuses and full basic route families. Many still share repeated branch shapes, repeated icon groups, and helper-based generic reward flow. |
| Compact crisis splinters | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` in `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Mixed | PRA is now cleaner by layout/filter. TSC/RMC/DSC/NRF/ICD remain 18-focus compact trees and need deeper high-chaos identity if expected to be overpowered/aggressive actors. |
| Old Great Bulgaria | `OGB_soviet_collapse_focus_tree`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1176`, 23 focuses | Shallow | Has Volga legitimacy and restored-name content, but remains under-depth for the spec's Volga restoration expectations. |
| Military Factory of Russia | `MFR_soviet_collapse_focus_tree`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1784`, 58 focuses | Stronger but layout-risky | Arsenal identity and direct mechanics are stronger than OGB, but it still has 14 likely pathline hits and helper-heavy rewards. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` in `common/national_focus/005_soviet_collapse_ancient_restorations.txt:14`, `:383`, `:753`, `:1126` | Compact/shallow | Each has 16 focuses with claims and route flags, but they are still compact restorations rather than full political/industry/military/diplomacy/expansion packages. |

## Missing or Simplified Content

- No direct duplicate `add_ideas` calls were found inside individual focus rewards in the four focus files.
- Repeated idea-helper pressure remains in `common/scripted_effects/005_soviet_collapse_effects.txt:5466`, where `soviet_collapse_update_consolidated_republic_ideas` cycles through four institution, League, foreign-support, and local-authority idea ladders. This is centralized and mostly hidden, but it still gives many helper-heavy focuses a same-feeling national-spirit payoff.
- `PRA_rails_over_capitals`, `DSC_claim_the_soldiers_road`, `DSC_armies_that_do_not_demobilize`, `DSC_congress_of_the_dead_army`, `TSC_starfall_mandate`, `RMC_resurrection_without_state`, `NRF_northern_revenant_fleet`, and `ICD_commissariat_without_end` each stack four to six helper calls in one reward block. This is powerful, but the hover/behavior can still feel like bundled helper spam instead of a visible route mechanic.
- `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` remain 18-focus crisis trees. Their high-chaos concepts should be more aggressive and route-defining if they are expected to be major threats.
- `OGB_soviet_collapse_focus_tree` remains only 23 focuses and needs a larger Volga restoration branch set or an explicit scope-down note.
- Ancient restorations remain compact at 16 focuses each. They have claims and route flags, but not enough depth for long-lived playable restorations.
- Repeated generic small rewards remain common: political power, stability, war support, one-off equipment, and helper calls appear across many branches.

## Icon Coverage Table

| File | Focuses checked | Missing icon assignments | Repeated icon groups | Repeated icon uses | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 22 | 65 | Repeated icons remain in republic/shared trees. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 99 | 219 | Biggest repeated-icon surface. No asset or icon-file patch made by request. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 11 | 26 | CFR has known repeated icons; OGB/MFR direct audit still shows layout/depth risks. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 8 | 30 | Shared ancient icon families make compact restorations feel template-like. |

Repeated icon clusters to prioritize later without touching assets in this pass:

- Republics: `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`, `GFX_moldova_soviet_collapse_ukrainian_corridor`.
- Custom splinters: repeated generic route icons in `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, plus smaller repeats in `BAC`, `ARD`, `NLC`.
- Ancient restorations: `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_guard_old_routes`, `GFX_focus_soviet_collapse_ancient_league_bargain`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_symbolic_state`.

## Layout Findings

Mechanical scan after the PRA patch:

- 1,698 focuses across 41 focus trees.
- Duplicate focus coordinates: 0.
- Upward prerequisites: 0.
- Same-row prerequisites: 0.
- Adjacent mutual-exclusion pairs: 0.
- Missing search filters: 0.
- Missing `ai_will_do` blocks: 0.
- PRA pathline hits: reduced from 2 to 0.

Remaining likely pathline-hit counts by tree family:

- High-risk broad trees: Ukraine 41, Kazakhstan 45, Belarus 25, Baltic 23, Moldova 22.
- Moderate shared trees: Internal republics 12, Caucasus 12, Central Asia 12, generic breakaway 9.
- Custom splinters: many have 3-13 likely hits, especially `NLC` 13, `UWD` 13, `DHC`/`KHC`/`IUL` 11, `MRC` 10.
- Factory/ancient: `MFR` 14, `OGB` 5, each ancient restoration 1.

Continuous focus panel risk:

- Very wide trees with `continuous_focus_position` near the active tree surface should get screenshot validation later: Ukraine, Internal republics, Baltic, Belarus, Kazakhstan, CFR, and possibly MFR.
- No continuous panel positions were changed in this pass.

## Localisation and Reward Mismatch List

- Full localisation coverage exists for all 1,698 focus ids when all `localisation/english/*005_soviet_collapse*_english.yml` files are included. The two minimum files named by the parent do not contain every focus key by themselves; Ukraine and regional focus strings live in separate Event 005 focus localisation files.
- `PRA_claim_the_branch_lines` had a filter/reward mismatch: political/army filters versus rail/logistics rewards. Patched to `FOCUS_FILTER_INDUSTRY`.
- Many filter mismatch candidates remain if checking only direct reward keywords, but many are false positives because the effects are behind scripted helpers. The main unresolved design issue is helper opacity, not necessarily invalid filter syntax.
- Focus names and descriptions are generally present, but several route titles promise larger mechanics than the reward block visibly shows because helper bundles hide the actual payoff.

## AI Behavior Gaps

- Every parsed focus has an `ai_will_do` block.
- Many AI blocks remain flat or near-flat base weights, especially in ancient restorations and some republic trees. Kazakhstan has 61 flat/low-context AI blocks by static scan.
- High-chaos/custom splinter AI needs more explicit aggression when it has the correct route flags, chaos tier, war state, and targets.
- Republic AI still needs stronger route-aware choices for League alignment, foreign dependency, expansion, high-chaos escalation, and local defense.
- Detailed AI strategy should follow route expansion; otherwise it will lock in shallow current behavior.

## High-Priority Fixes First

1. Do a focused non-Ukraine layout pass on Kazakhstan, Belarus, Baltic, Moldova, and MFR pathline clusters. These are mechanically safe but should be done in bounded batches.
2. Expand or explicitly scope down `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree`.
3. Expand `OGB_soviet_collapse_focus_tree` or document it as intentionally compact despite the larger Volga-restoration spec.
4. Give high-chaos splinter endgame focuses more visible direct mechanics: target claims/war goals, unit packages, AI strategies, route decisions, postwar handling, or event hooks instead of only helper bundles.
5. Reduce idea-helper sameness by replacing some repeated helper-only rewards with decisions, missions, state construction, state targets, unit templates, or custom tooltips that describe the concrete route action.
6. Run an icon identity pass later, but only when visual asset work is explicitly allowed.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_172146_event005_focus_tree_current_audit_pra_layout_filter_patch.md`: passed.
- Brace-balance check for `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `final_depth=0`, no early closes.
- Unsupported comparison-operator search for `common/national_focus/005_soviet_collapse_custom_splinters.txt` and this handoff: no matches.
- Localisation BOM check skipped because no localisation file was edited.
- `git diff --name-only -- gfx/flags`: empty output.

## Skipped Validation

- No in-game launch or screenshot validation was run.
- No icon, sprite, interface, flag, or image validation was run because visual assets were explicitly out of scope.
- No Ukraine layout patch was attempted because the parent is actively touching Ukraine.

## Remaining Route Risks

- The focus implementation is much cleaner than earlier audits, but final completion is still not supportable: broad route depth, helper opacity, repeated icons, and layout pathlines remain.
- The current worktree has many pre-existing Event 005 and Event 006 changes, including visual asset changes outside this pass. This handoff only proves that this pass did not add or edit `gfx/flags` or visual asset files.
- Existing broader plan still applies: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
