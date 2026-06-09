# Event 005 Focus Tree Audit and Ancient Prerequisite Patch Handoff

Date: 2026-05-31
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Read and Reference Context

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding. `Effects - Hearts of Iron 4 Wiki.md` was not present under that exact title; vanilla `effects_documentation.md` was used for effect references.
- Vanilla references: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `common/national_focus/generic.txt`.
- Event source docs: `docs/events/005_soviet_collapse.md`, `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`, and existing plan `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

## Current-State Audit Summary

Parser pass over the four focus files found:

- 41 focus trees, 1,698 focuses.
- 0 duplicate focus ids.
- 0 missing focus icon assignments.
- 0 missing `completion_reward` blocks.
- 0 missing `ai_will_do` blocks.
- 0 missing `search_filters` blocks.
- 0 missing focus name or description localisation keys in `localisation/english/005_soviet_collapse*.yml`.
- 0 duplicate same-tree coordinates.
- 0 same-row or upward prerequisite path risks after this patch.
- 0 direct `add_ideas` focus rewards in the parsed focus files.

Icon sprite existence was not checked by reading `interface/` or asset files because the task explicitly said not to touch flags, gfx, interface, sprite, image, music, sound, or asset files. Icon assignment coverage was checked from the focus files only.

## Route Coverage Table

| Required route or tree family | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine republic | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial | Real political, League, bread-state, military, foreign, industry, and expansion lanes exist. Still dense and helper-heavy: 53 helper-oriented rewards, 21 helper rewards with little direct visible payload. Avoided patching Ukraine per scope caution. |
| Generic breakaway republic | `soviet_collapse_breakaway_focus_tree`, 36 focuses | Partial | Usable emergency/recovery tree, but route identity is generic and 15 helper-no-direct rewards remain. |
| Internal Soviet republic | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Partial | Has internal leadership, military, port, foreign, and league-ish branches. Still has many helper rewards and limited route-specific AI beyond focus weights. |
| Baltic successor package | `soviet_collapse_baltic_focus_tree`, 42 focuses | Partial | Legal-state, front-state, port, border, and foreign branches exist. Decision/mechanic integration remains lighter than the route names imply. |
| Caucasus successor package | `soviet_collapse_caucasus_focus_tree`, 40 focuses | Partial | Mountain federal/national restoration, oil, passes, and foreign branches exist. Several OR prerequisites are intentional but need in-game readability review. |
| Central Asian successor package | `soviet_collapse_central_asia_focus_tree`, 45 focuses | Partial | Oasis, southern-shield, Basmachi, federation, and old-movement hooks exist. Some branch payoffs still resolve as shared variables/helpers. |
| Moldova successor package | `soviet_collapse_moldova_focus_tree`, 48 focuses | Partial | River, Prut, Romanian, Ukrainian corridor, and league branches exist. Some hidden route semantics still need player-facing clarity. |
| Belarus successor package | `soviet_collapse_belarus_focus_tree`, 53 focuses | Partial | Rail, forest, corridor, military transit, national/socialist/foreign routes exist. Layout parses cleanly, but the tree remains dense and helper-heavy. |
| Kazakhstan successor package | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses | Partial | Deepest non-Ukraine republic tree with Alash, socialist, resource, southern, foreign, league, and military lanes. Still has 64 helper-oriented rewards and many route AI weights remain flat. |
| Full custom splinter trees | FTH, BSC, TNC, ALA, BBH, KRS, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, NLC; mostly 47 focuses each | Partial | Most have real branch structures and expansion hooks, but many rewards remain helper-oriented and repeated. Several use 12-15 reused icon assignments in a single tree, especially FEV/SZA/UWD/IUL/MRC. |
| Compact chaos trees | PRA 22 focuses; TSC/RMC/DSC/NRF/ICD 18 focuses each | Partial/Risk | These are mechanically cleaner than stubs but are still compact crisis ladders, not full strong/aggressive country trees. DSC is strongest mechanically; TSC/RMC/ICD remain the shallowest. |
| Factory successors | CFR 47, OGB 23, MFR 58 | Partial/Risk | CFR and MFR have real forks. OGB remains the clearest factory-successor depth risk: 23 focuses and only light route branching. |
| Ancient restorations | KZR/SOG/KHW/ALN, 16 focuses each | Partial/Risk | All four have compact identity, claim, symbolic-vs-expansionist fork, charter, and endgame hooks. They are still shallow compared with the requested ancient-restoration promise. |

## Missing or Simplified Content

- Ancient restorations are still 16-focus compact packages. They need larger route design before they can be called complete restoration trees.
- OGB is still a 23-focus successor and should receive a deeper Volga/old-name/industrial/military/expansion route pass or be explicitly documented as intentionally narrow.
- TSC/RMC/ICD are compact chaos crisis trees with limited internal politics, industry, and distinct decision surfaces.
- Focus rewards are much less idea-spammy now, but many remain opaque because the player sees helper effects, variable changes, flags, claims, or stockpiles instead of visible decision/mission evolution.
- Route-specific AI mostly exists as per-focus `ai_will_do`; broad AI strategy behavior remains thin for political route choice, expansion timing, and restraint/escalation by campaign state.

## Icon Coverage Table

| File | Focuses | Missing icon assignments | Reused icon assignments | Notes |
| --- | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | Present | Reuse is moderate. Ukraine, internal republic, Belarus, and Kazakhstan have some repeated generic route icons but no missing assignments. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | High in several trees | FEV, SZA, UWD, MRC, IUL have 12-15 reused icon ids in-tree; this is an identity polish risk. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | CFR has 11 reused icon ids | CFR reuse is noticeable; OGB/MFR have unique assignments by parser. |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | Shared ancient generic icons by design | No missing assignments; four compact trees intentionally share some ancient generic icons. Sprite existence not checked due no-touch asset/interface constraint. |

## Localisation and Reward Mismatch List

- Localisation coverage: no missing focus title/description keys found for the 1,698 parsed focus ids.
- The largest mismatch class is not missing text, but reward opacity: focus names promise institutions, charters, route governments, old borders, League bargains, or high-chaos identity while many rewards call shared helpers or adjust variables without a direct visible unlock.
- Current helper-heavy examples by tree: Ukraine 53 helper-oriented rewards, Kazakhstan 64, MFR 48, CFR 35, Belarus 37, Moldova 35, internal republic 30.
- Ancient restorations now expose hidden old-border requirements as prerequisites, but 8-9 helper-no-direct rewards remain in each 16-focus tree.

## AI Behavior Gaps

- Every parsed focus has an `ai_will_do` block.
- Most `ai_will_do` blocks are base weights plus a small number of local modifiers. They do not yet amount to route-aware AI strategy for political route selection, expansion windows, foreign patron risk, League alignment, old-name escalation, or compact crisis behavior.
- Ancient expansionist focuses add hidden anti-SOV AI strategies, but this is not a full route plan for neighboring targets or postwar handling.
- Compact chaos trees need AI that treats them as extremely aggressive special countries, not just ordinary focus pickers.

## High-Priority Fixes First

1. Deepen or explicitly classify ancient restorations: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, `ALN_soviet_collapse_ancient_focus_tree`.
2. Deepen OGB: `OGB_soviet_collapse_focus_tree` is still short relative to the user complaint.
3. Give TSC/RMC/ICD route-specific mechanics and stronger direct aggression: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`.
4. Reduce helper opacity in the large republic and factory trees, especially `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_kazakhstan_focus_tree`, `MFR_soviet_collapse_focus_tree`, `CFR_soviet_collapse_focus_tree`, and `soviet_collapse_belarus_focus_tree`.
5. Add route-aware AI strategy behavior for major route selectors and chaos expansion paths.

## Patch Applied

Changed file:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Changed focus ids:

- `KZR_old_border_files`
- `SOG_old_city_border_files`
- `KHW_old_oasis_border_files`
- `ALN_old_pass_border_files`
- `ALN_symbolic_pass_principality`

Route behavior before:

- The four old-border-file focuses had one visible prerequisite from the League bargain focus, then hid the required industry/guard branch completions inside `available = { has_completed_focus = ... }`.
- This made the tree look like the route could proceed from the bargain alone while the tooltip contained extra route locks.
- `ALN_symbolic_pass_principality` had indentation drift inside the focus block.

Route behavior after:

- The industry/guard branch requirements are visible focus prerequisites on all four old-border-file focuses.
- The old-border-file focuses still require the same completed focuses as before; the change makes the existing AND requirements visible in the focus tree pathlines instead of hiding them in `available`.
- `ALN_symbolic_pass_principality` indentation now matches the surrounding focus style.

Localisation keys changed: none.

Icon ids changed: none.

Scripted effects changed: none.

Asset/interface/gfx/flag files changed: none.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: passed.
- Brace balance over all four scoped focus files: final depth 0, no early closes.
- Parser pass over all four scoped focus files: 41 trees, 1,698 focuses, 0 duplicate focus ids, 0 missing localisation name/desc keys, 0 missing icon assignments, 0 missing rewards, 0 missing AI, 0 missing search filters, 0 duplicate coordinates, 0 same-row/upward prerequisites.
- `rg -n '<=|>='` over all four scoped focus files: no matches.
- `git diff --name-only -- gfx/flags`: empty.

Skipped validation:

- Localisation BOM check skipped because no localisation file was touched.
- Sprite definition existence check skipped because interface/gfx/asset files were out of scope and explicitly no-touch.
- In-game visual pathline screenshot validation skipped; no local HOI4 render pass was available in this subagent turn.

## Remaining Route Risks

- The broader complaint is valid: many trees are no longer broken stubs, but several still feel like helper-driven route ladders rather than identity-specific countries.
- Ancient restorations and OGB remain the clearest shallow-content risks.
- Compact chaos trees need stronger direct expansion, internal command, industry, military, and decision branches if the target is "extremely strong/aggressive."
- Existing broad redesign plan remains relevant: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

## Dirty Worktree Note

The parent already had dirty focus files. This pass only intentionally changed the ancient prerequisite visibility and the Alan indentation block listed above, plus this handoff. Existing dirty diff in the same focus files should not be attributed to this pass without separate review.
