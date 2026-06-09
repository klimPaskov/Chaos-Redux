# Event005 Focus Reward And Layout Audit Patch Handoff

Date: 2026-05-31 19:19:24 UTC

Scope: bounded audit of Event005 Soviet Collapse focus rewards and layout in:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

The prior handoff `2026_05_31_event005_focus_tree_reward_layout_patch_handoff.md` was read first. This pass did not duplicate those exact focus reward/layout patches. No `gfx/flags` files or flag assets were read or edited.

## Files Changed

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Moved one Belarus timetable focus down one row to clear a mutual-exclusion line. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Added concrete local map/logistics rewards to two shallow northern settlement focuses. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_191924_event005_focus_reward_layout_audit_patch_handoff.md` | This handoff. |

No scripted effects, decisions, localisation, icon definitions, GFX, or flags were edited.

## Changed Focus IDs

| Focus id | File | Before | After |
| --- | --- | --- | --- |
| `blr_soviet_collapse_timetable_state` | `005_soviet_collapse_republics.txt` | Sat at `x = 9, y = 5`, directly between mutually-exclusive Belarus route choices `blr_soviet_collapse_national_council_of_minsk` and `blr_soviet_collapse_socialist_autonomy_without_moscow`. | Moved to `y = 6`, clearing the same-row mutual-exclusion symbol/pathline without changing prerequisites or rewards. |
| `ARD_murmansk_port_records` | `005_soviet_collapse_custom_splinters.txt` | Mostly abstract settlement reward: stability, recognition, navy XP, liaison reach, and legal-recognition helper. | Also grants convoys and builds a dockyard plus infrastructure in a coastal owned controlled state with a free dockyard slot. |
| `NLC_polar_neutrality_statute` | `005_soviet_collapse_custom_splinters.txt` | Stability plus legal-recognition helper only. | Also adds resilience, liaison reach, and a local infrastructure/radar/AA buildout. |

## Route Behavior Before And After

| Route surface | Before | After |
| --- | --- | --- |
| Belarus route-choice row | One non-route focus occupied the same row and x-span as a route mutual-exclusion link. | The timetable focus sits one row lower; parser reports no remaining same-row mutual-exclusion blockers in the scoped files. |
| Arctic Directorate settlement route | `ARD_murmansk_port_records` read like a port/logistics focus but did not create a port-side asset or convoy payoff. | Murmansk records now visibly strengthen a coastal industrial/logistics base and convoy pool. |
| Northern Lights Commune settlement route | `NLC_polar_neutrality_statute` was a shallow recognition/stability reward. | The neutrality statute now creates a defended communications post and improves resilience/liaison variables. |

## Route Coverage Table

| Required route/family | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Major republic runtime trees | Ukraine, breakaway/internal republics, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan in `005_soviet_collapse_republics.txt` | Implemented but uneven | 9 trees / 501 focuses. No missing basic focus surfaces found. Several rewards remain helper-heavy and need parent-level route review against the full spec. |
| Custom high-chaos splinters | 25 trees in `005_soviet_collapse_custom_splinters.txt` | Implemented but still repetitive | 1005 focuses. Many 47-focus trees exist, while PRA/TSC/RMC/DSC/NRF/ICD remain compact. Some compact trees are intentionally focused, but route depth still needs parent review. |
| Factory successors | CFR, OGB, MFR in `005_soviet_collapse_factory_successors.txt` | Implemented; OGB compact | 128 focuses. CFR/MFR have deeper trees; OGB remains 23 focuses and should be explicitly accepted as compact or expanded. |
| Ancient restorations | KZR, SOG, KHW, ALN in `005_soviet_collapse_ancient_restorations.txt` | Implemented but shallow by major-depth standards | 64 focuses total. These are still 16-focus compact trees and are not enough for a full route-depth completion claim. |

## Missing Or Simplified Content

| Issue | File / identifiers | Priority | Notes |
| --- | --- | --- | --- |
| Broad helper-heavy rewards remain | Examples: `ukr_soviet_collapse_border_states_accept_kyiv`, `FTH_endgame`, `PRA_rails_over_capitals`, `DSC_congress_of_the_dead_army`, `SZA_station_fortress_line`, `OGB_the_old_name_survives_modern_war` | High | Focus-file callsite audit found many focuses with three or more major helper calls. That can still produce visible reward stacks or idea-update spam depending on helper internals. Full cleanup requires scripted-effect inspection and helper consolidation outside this subagent scope. |
| Ancient restoration depth remains compact | `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree` | High | No whole-tree redesign was attempted. These should be expanded or explicitly classified as compact restoration packets. |
| OGB depth remains compact | `OGB_soviet_collapse_focus_tree` | Medium | 23 focuses; likely underpowered compared with CFR/MFR unless the parent accepts the compact role. |
| Generic identity-helper-only nodes remain | Examples include `ARD_special_arm`, `ARD_supply`, `NLC_civil_rule`, repeated 47-focus generic route openers | Medium | Many route identity focuses still rely on `custom_effect_tooltip` plus hidden identity helper only. Replacing all of these is a broad route-reward pass. |

## Idea Spam And Helper Stack Audit

| Check | Result |
| --- | --- |
| Duplicate direct `add_ideas` or repeated direct `modify_ideas` inside a single focus reward | None found in the four scoped files. |
| Repeated identical custom helper call inside a single focus reward | None found after filtering parser false positives. |
| Multiple major helper calls inside one reward | Still common. These are callsite-level risks for visible helper reward stacks and repeated idea updates. |
| Confirmed helper internals adding/updating the same idea | Not confirmed in this pass because scope was limited to the focus files only. This remains uncertain until the parent inspects the scripted helpers. |

High-priority helper-stack examples for parent follow-up:

| Focus id | Helper stack |
| --- | --- |
| `PRA_rails_over_capitals` | chaos assault plan + rail authority + expansion claims + assault columns + endgame completion |
| `DSC_armies_that_do_not_demobilize` | road claims/cores + chaos assault + objective pressure + war launcher + assault columns |
| `DSC_congress_of_the_dead_army` | chaos assault + expansion claims + assault columns + war launcher + endgame completion |
| `SZA_station_fortress_line` | rail authority + mobile columns + expansion claims + neighbor conflict plan |
| `OGB_the_old_name_survives_modern_war` | endgame completion + objective pressure + expansion claims |

## Icon Coverage Table

| Surface | Result |
| --- | --- |
| Missing focus icons | None found by parser in the four scoped files. |
| Missing `completion_reward`, `search_filters`, or `ai_will_do` | None found by parser in the four scoped files. |
| Repeated icons | Still present but less severe than previous file-wide counts when audited per tree. Highest examples: `GFX_focus_FEV_diplomatic_plan` x4, `GFX_focus_MRC_foreign` x4, `GFX_focus_MRC_civil_rule` x4, `GFX_focus_IUL_war_plan` x4, `GFX_ukr_soviet_collapse_democratic` x4, `GFX_central_asia_soviet_collapse_steppe_federation` x4. |
| Icon or GFX edits made | None. |

## Localisation And Reward Mismatch List

No focus ids, localisation keys, or icon ids were added or renamed, so localisation was not edited.

| Focus id | Mismatch before | Current status |
| --- | --- | --- |
| `ARD_murmansk_port_records` | Name implied port records/logistics, but reward was mostly abstract recognition and legal-recognition helper. | Now has convoy, dockyard, and infrastructure payoff. |
| `NLC_polar_neutrality_statute` | Name implied a hardened neutrality settlement, but reward was only stability and legal recognition. | Now has resilience, liaison, radar, AA, and infrastructure payoff. |
| Remaining generic identity focuses | Many still use hidden route identity helper plus generic tooltip. | Not patched; broad reward redesign required. |

## AI Behavior Gaps

All scoped focuses have `ai_will_do`, but many remain shallow.

| Area | Gap |
| --- | --- |
| 47-focus custom splinters | Many route choices use flat base weights or only one pressure check. They need route-aware behavior based on war state, industry, Soviet objective pressure, recognition, and branch flags. |
| Ancient restorations | AI exists but is mostly flat; symbolic versus expansionist choices should react to war, state control, recognition, and League state. |
| OGB | Compact tree has AI weights but not enough route-specific strategic pressure compared with CFR/MFR. |
| High-chaos routes | AI should avoid extreme escalation unless chaos tier, old-movement pressure, and campaign instability justify it. |

## High-Priority Fixes First

1. Inspect the scripted helper definitions for the high helper-stack focuses above and collapse duplicated idea-update calls where helpers overlap.
2. Decide whether ancient restorations and OGB are accepted compact trees or must be deepened.
3. Replace the remaining identity-helper-only rewards with concrete map, unit, decision, war-goal, or postwar effects.
4. Add route-aware AI strategy beyond flat per-focus weights for custom splinters and ancient restorations.
5. Schedule an icon pass for repeated icons. Do not touch flags.

## Validation Run

Passed:

```text
python3 brace-depth check:
common/national_focus/005_soviet_collapse_republics.txt: brace_depth=0 bad=[]
common/national_focus/005_soviet_collapse_custom_splinters.txt: brace_depth=0 bad=[]
common/national_focus/005_soviet_collapse_factory_successors.txt: brace_depth=0 bad=[]
common/national_focus/005_soviet_collapse_ancient_restorations.txt: brace_depth=0 bad=[]

git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
no output

corrected focus parser:
missing icon/reward/ai/filter: 0
layout issues: 0

git diff --name-only -- gfx/flags
no output
```

Skipped validation:

- No live HOI4 load test; subagent environment only.
- No scripted helper internals were inspected because the prompt limited inspection to the four focus files.
- No localisation encoding check or localisation edit because no localisation files were touched.
- No flag validation beyond confirming the flag diff is empty; flags were explicitly out of scope.

## Remaining Risks

- The worktree was already dirty before this pass, including these Event005 focus files. Parent should review the combined diff carefully before committing.
- Helper-driven idea spam cannot be fully proven or removed from focus callsites alone. The parent needs a scripted-effect pass for the helper stacks.
- The two reward patches are intentionally small and local; they do not solve the larger complaint that several chaos-country routes still need to be stronger and less generic.
