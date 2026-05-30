# Event 005 Focus Tree Audit and Helper Tooltip Patch Handoff

Date: 2026-05-30  
Agent: Chaos Redux focus tree subagent  
Scope: Event 005 Soviet Collapse focus trees only. No flags, image files, `gfx/`, or interface sprite assets were edited.

## Files Changed

| File | Change |
|---|---|
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Hid two high-chaos endcap helper bundles behind existing custom tooltips. |

No localisation keys, icon ids, decision ids, idea ids, flags, visual assets, or `.gfx` sprite definitions were changed by this pass.

## Focus IDs and Helpers Touched

| Focus id | Helpers moved into `hidden_effect` | Visible behavior before | Visible behavior after |
|---|---|---|---|
| `PRA_rails_over_capitals` | `soviet_collapse_apply_focus_high_chaos_identity`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_rail_authority_reward`, one rail construction effect | Tooltip exposed several direct helper effects plus the route tooltip. | Focus still shows `pra_declare_the_moving_state`, the Soviet war goal when valid, and `soviet_collapse_custom_splinter_route_identity_reward_tt`; helper details execute silently. |
| `RMC_resurrection_without_state` | `soviet_collapse_apply_focus_high_chaos_identity`, `soviet_collapse_apply_focus_military_consolidation` | Tooltip exposed direct high-chaos and military helper effects plus the route tooltip. | Focus still shows the Soviet war goal when valid and `soviet_collapse_custom_splinter_route_identity_reward_tt`; helper details execute silently. |

The endgame helper calls remain visible: `soviet_collapse_complete_pale_railway_endgame` and `soviet_collapse_complete_red_martyrs_endgame`.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
|---|---|---|---|
| Republic political, industry, expansion, diplomacy, military, high-chaos where relevant | 9 republic/internal/shared trees, 501 focuses | Partial | Ukraine and Kazakhstan are broad; Belarus and shared republic trees still need route readability and reward-identity review. |
| Custom splinter political/industry/expansion/special branches | 25 custom splinter trees, 1005 focuses | Partial | Most full splinters have 47 focuses. Crisis splinters `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` remain much shallower at 18-22 focuses. |
| Factory successors with industrial and high-chaos successor identity | `CFR`, `OGB`, `MFR`, 128 focuses | Partial | `CFR` and `MFR` have visible forks. `OGB` remains a 23-focus shallow high-chaos successor relative to the spec. |
| Ancient restoration modern administration, ancient claim, army, diplomacy, expansion, myth pressure | `KZR`, `SOG`, `KHW`, `ALN`, 64 focuses | Partial | Each ancient restoration is still a 16-focus compact tree and needs deeper route mechanics before completion can be claimed. |
| High-chaos countries strong and aggressive | High-chaos helpers, war goals, claims, assault columns, and AI strategies appear across splinter endcaps | Partial | Aggression exists, but several route payoffs still read as stacked helper bundles instead of bespoke mechanics. |

## Audit Counts

| File | Trees | Focuses | Direct `add_ideas` in focus rewards | Visible helper-heavy focuses, 3+ visible helper calls | OR-prereq converges mutual pair |
|---|---:|---:|---:|---:|---:|
| `common/national_focus/005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 24 | 4 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 22 | 26 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 0 | 1 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | 0 | 0 | 4 |

Total current focus count: 1698.  
Total current direct visible idea additions from focus rewards: 0.  
Total current visible helper-heavy focuses using the 3+ visible-helper threshold: 46.

## Icon Coverage Table

| File | Focuses with icon | Missing icon assignments | Unique icon ids | Repeated icon ids | Duplicate icon assignments |
|---|---:|---:|---:|---:|---:|
| `common/national_focus/005_soviet_collapse_republics.txt` | 501 | 0 | 458 | 22 | 43 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 885 | 99 | 120 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 128 | 0 | 113 | 11 | 15 |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 42 | 8 | 22 |

Icon assignments exist everywhere, but repeated icon families remain common. Per the latest user constraint, no icon, flag, asset, sprite, `.gfx`, or image path was edited.

## Missing or Simplified Content

- `OGB_soviet_collapse_focus_tree` remains shallow at 23 focuses for a high-chaos successor and still needs deeper trade, religion/society, rival, expansion, and late-game route mechanics.
- `KZR`, `SOG`, `KHW`, and `ALN` ancient restoration trees remain 16-focus compact trees and do not yet satisfy the full ancient-restoration route promise.
- Crisis splinters `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are mechanically present but still more like crisis packages than full political/industrial/expansion trees.
- 35 focus joins use an OR prerequisite over mutually exclusive focuses. Some are intentional convergence points, but they should be reviewed for visible pathline clarity. First examples: `ukr_soviet_collapse_free_soil_compromise`, `FTH_industry_plan`, `CFR_apartment_blocks_for_loyalty`, `KZR_khazar_charter`.
- Visible helper spam remains in 46 focuses by the 3+ visible-helper threshold, especially Ukraine endcaps and custom splinter endcaps.

## Localisation and Reward Mismatch List

- Missing focus localisation: 0 across all `005_soviet_collapse*` English localisation files.
- Missing focus descriptions: 0 across all `005_soviet_collapse*` English localisation files.
- Duplicate event-localisation keys found by script: only repeated `l_english` headers across multiple files, expected.
- Specific patched tooltip key reused: `soviet_collapse_custom_splinter_route_identity_reward_tt`.
- No text/reward mismatch was patched in this pass. The remaining risk is qualitative: generic route tooltip text covers several hidden helper bundles and is safe for hover cleanup, but bespoke endcap tooltips would be clearer in a larger polish pass.

## AI Behavior Gaps

- Every audited focus has an `ai_will_do` block.
- High-chaos endcaps often have aggression strategies and chaos-tier modifiers, but route-aware AI remains uneven: many focuses still use simple `base` weights with one or two broad modifiers.
- `PRA_rails_over_capitals` and `RMC_resurrection_without_state` still add anti-Soviet `conquer` and `antagonize` strategies in hidden effects; their AI behavior is unchanged by this patch.
- Broader route AI should still react more consistently to war state, Soviet collapse pressure components, regional faction membership, and route flags.

## High-Priority Fixes Remaining

1. Deepen `OGB_soviet_collapse_focus_tree` or document why it is intentionally narrow.
2. Expand ancient restoration trees beyond 16-focus shells with real modern/ancient/army/diplomacy/expansion/high-chaos mechanics.
3. Review the 35 OR-convergence mutual-exclusion joins for pathline clarity and route semantics.
4. Continue hiding or consolidating visible helper bundles in the 46 remaining helper-heavy focuses.
5. Replace remaining generic equipment/truck/convoy-style rewards with route mechanics, decision unlocks, state construction, missions, or bespoke payoff helpers.
6. Improve route-aware AI beyond base weights, especially for high-chaos and foreign-patron routes.

## Validation Run

- Brace-depth check on all four focus files: depth 0, minimum depth 0.
- Unsupported operator scan for `<=` and `>=` across scoped focus/effect/decision/idea/localisation files: no matches.
- Current focus count script: 1698 focuses.
- Missing focus icon assignment script: 0.
- Missing `ai_will_do` script: 0.
- Missing `search_filters` script: 0.
- Missing focus localisation/name/description script across all `005_soviet_collapse*` English localisation files: 0.
- Direct `add_ideas` in focus completion rewards: 0.
- `git diff --name-only -- gfx/flags`: empty.

Skipped validation:

- No in-game load or visual focus-tree screenshot validation was run. This pass was a bounded subagent audit/patch in a heavily dirty parent worktree.
- No flag or visual asset validation was performed because the latest constraint forbids touching flags or visual assets.

## Remaining Route Risks

- Existing dirty changes in the same files predate this pass; this handoff only claims the two helper-tooltip edits above.
- There are pre-existing dirty interface and `gfx/achievements` / `gfx/super_events` paths in the worktree, but this pass did not edit them.
- The current tree set is improved from earlier shallow drafts but still does not meet the full objective for all Event 005 focus trees.

## Plan Handoff

No new broad improvement plan was written. The existing broader plan remains the active handoff:

`docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

