# Soviet Collapse Focus Current-State Panel Clearance Audit

Date: 2026-05-29
Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs/examples: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`, and vanilla focus examples in `~/projects/Hearts of Iron IV/common/national_focus/`.

## Patch Summary

The current worktree already contains broad Soviet Collapse focus work. This pass only made a safe layout clearance patch in `005_soviet_collapse_republics.txt`; no route redesign, reward redesign, localisation edit, icon edit, scripted helper edit, or decision edit was made.

Changed continuous focus panels:

| Tree | Before | After | Reason |
| --- | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | `x = 3648 y = 180` | `x = 3840 y = 180` | Rightmost focus is at `x = 34`; the panel had only four grid units of clearance. |
| `soviet_collapse_internal_republic_focus_tree` | `x = 2976 y = 180` | `x = 3264 y = 180` | Rightmost focus is at `x = 27`; the panel had only four grid units of clearance. |
| `soviet_collapse_belarus_focus_tree` | `x = 2976 y = 180` | `x = 3264 y = 180` | Rightmost focus is at `x = 28`; the panel had only three grid units of clearance. |
| `soviet_collapse_kazakhstan_focus_tree` | `x = 3648 y = 180` | `x = 3936 y = 180` | Rightmost focus is at `x = 35`; the panel had only three grid units of clearance. |

Changed focus ids: none. The patch only moved tree-level `continuous_focus_position` values.

Localisation keys changed: none.

Icon ids changed: none.

## Route Coverage Table

| Required route/content area | Current coverage | Status | Notes |
| --- | --- | --- | --- |
| Ukraine politics/state identity | 83-focus tree with democratic, socialist, directory, League, Black Banner, protectorate, grain, military, industry, and expansion lanes. | Partial | Current topology validates cleanly, but the tree is still very broad and needs in-game readability review. |
| Belarus rail/forest/corridor identity | 53-focus tree with rail, corridor, foreign transit, League freight, forest defense, and army/partisan branches. | Partial | No duplicate or too-close parser coordinates remain; manual screenshot review still needed because the design is dense. |
| Standard republic families | Breakaway, internal republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan are implemented. | Partial | Rewards still lean heavily on shared helpers and variable progress. |
| Custom chaos splinters | 25 custom splinter trees exist; most have 47 focuses, crisis trees have 18-22. | Partial | DSC already has manpower, claims/cores-on-control, neighbor war goals, anti-SOV AI, and assault-column spawning, but short crisis trees remain less deep than full major-country trees. |
| Factory successors | CFR, OGB, MFR trees exist. | Partial | CFR/MFR have identity forks; OGB remains shorter than the full design target. |
| Ancient restorations | KZR, SOG, KHW, ALN trees exist. | Partial | Each is a compact 16-focus package and should not be called full-depth restoration content. |

## Missing or Simplified Content

- No direct duplicate `add_ideas` spam was found in focus rewards during this pass.
- Focus-decision integration remains thinner than the design target in many trees. Several focuses use helper effects and variables rather than direct visible decision or mission evolution.
- Short crisis trees (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) are mechanically stronger than earlier stubs but remain compact crisis ladders. A full redesign would be broader than this bounded patch.
- Ancient restorations and `OGB` remain the clearest depth risks.

## Icon Coverage Table

| Metric | Result |
| --- | ---: |
| Focus trees parsed | 41 |
| Focuses parsed | 1,698 |
| Missing icon assignments | 0 |
| Missing focus name or description localisation in `005_soviet_collapse*` English localisation | 0 |
| Icon ids changed by this pass | 0 |

Repeated icon quality risks remain, especially in Ukraine, internal republics, Central Asia, Moldova, and several custom splinter trees. They are not load blockers and were not patched here.

## Localisation and Reward Mismatch List

- Missing focus name/description localisation: none found by the lightweight parser.
- No player-facing text was changed.
- Remaining mismatch risk: many focus titles promise institutions, route governments, League bargains, expansion, or high-chaos identity while the reward is still a shared helper, flag, variable, stockpile, or small construction effect. This needs a larger reward/decision integration pass.

## AI Behavior Gaps

- Every parsed focus has an `ai_will_do` block.
- Many AI blocks are still flat or only lightly state-aware.
- High-chaos and regional route AI needs more strategy-level behavior after any future route redesign: neighbor aggression, rail expansion, naval pressure, League participation, sponsor avoidance, and route-locked expansion choices.

## High-Priority Fixes

Completed:
- Moved Ukraine, internal-republic, Belarus, and Kazakhstan continuous focus panels right to reduce panel obstruction risk.

Not completed because it is broader than a safe bounded patch:
- Full Ukraine visual reflow.
- Full Belarus visual spacing redesign.
- Replacing shared-helper reward cadence across all routes.
- Adding broad decision, mission, postwar integration, or formable chains.
- Expanding short crisis and ancient-restoration trees into full route families.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: passed.
- `rg -n "<=|>=|FOCUS_FILTER_ARMY\\b|FOCUS_FILTER_AIR\\b|FOCUS_FILTER_NAVY\\b" ...`: no matches; command exited 1 because nothing was found.
- Brace-depth script over all four focus files: final depth `0`, no early closes.
- Focus parser over all four focus files: 41 trees, 1,698 focuses, 0 duplicate focus ids, 0 missing prerequisites, 0 duplicate coordinates, 0 same-row/upward prerequisite paths, 0 missing `ai_will_do`, 0 missing `completion_reward`, 0 missing icons, 0 missing focus name/description localisation.

## Skipped Validation

- No HOI4 launch test.
- No screenshot validation; panel and branch readability still need in-game review.
- No localisation encoding rewrite because localisation was not edited.
- No commit was created because the worktree contains many pre-existing concurrent edits, including the same target file; committing the file would include changes not made by this pass.

## Remaining Route Risks

The requested Soviet Collapse focus standard is not fully complete. This pass proves current files are mechanically cleaner than earlier audit notes and applies one safe panel-clearance patch, but it does not close the broader design risks around Ukraine readability, Belarus density, short crisis-tree depth, ancient-restoration depth, repeated helper rewards, route-aware AI, and decision/mission integration.
