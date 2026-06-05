# 2026-06-05 16:36 UTC - Focus Tree Auditor Current-State Complaint Audit

Subagent: `chaosx_focus_tree_auditor`

Task: current-state audit of Event005 Soviet Collapse focus trees after the latest parent patches, focused on the user complaints about idea/helper reward spam, unclear branch structure, insufficiently OP/aggressive chaos countries, and pathline/mutual-exclusion clutter, especially Ukraine, Kazakhstan, Belarus, and custom chaos/splinter trees.

## Scope And Rules

- Read-only gameplay audit. I made no focus, localisation, gfx, flag, interface, or asset changes.
- I did not touch `gfx/flags` or `interface/flags`.
- I inspected current files directly and did not rely on prior handoffs.
- I used the project focus-tree workflow and AGENTS.md-required references.

## Required References Consulted

- Offline Paradox wiki snapshot:
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
- Vanilla docs / precedent:
  - `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `~/projects/Hearts of Iron IV/common/national_focus/generic.txt`
- Repo skills:
  - `hoi4-focus-trees`
  - `chaos-redux-subagents`

## Files Inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/ai_strategy/005_soviet_collapse.txt`
- `common/ai_focuses/chaosx_ai_focuses.txt`
- `common/mtth/005_soviet_collapse_mtth.txt`

## Files Changed

- Added this handoff only:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_163631_focus_tree_auditor_current_state_complaint_audit.md`

No gameplay files were changed.

## Current Focus Tree Shape

Mechanical parse found 1,698 focus ids across the four Event005 focus files, with balanced braces and no missing checked focus references in prerequisites, mutual exclusions, relative positions, or `has_completed_focus` gates.

Focus-tree counts:

- `common/national_focus/005_soviet_collapse_republics.txt`
  - `soviet_collapse_ukraine_focus_tree`: 83 focuses, lines 19-2323.
  - `soviet_collapse_breakaway_focus_tree`: 36 focuses, lines 2326-3135.
  - `soviet_collapse_internal_republic_focus_tree`: 62 focuses, lines 3138-4655.
  - `soviet_collapse_baltic_focus_tree`: 42 focuses, lines 4658-5618.
  - `soviet_collapse_caucasus_focus_tree`: 40 focuses, lines 5621-6539.
  - `soviet_collapse_central_asia_focus_tree`: 45 focuses, lines 6542-7675.
  - `soviet_collapse_moldova_focus_tree`: 48 focuses, lines 7678-8817.
  - `soviet_collapse_belarus_focus_tree`: 53 focuses, lines 8820-10143.
  - `soviet_collapse_kazakhstan_focus_tree`: 92 focuses, lines 10146-12183.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - 25 custom/splinter trees.
  - `FTH` has 47 focuses, `PRA` 22, `TSC/RMC/DSC/NRF/ICD` 18 each, and most later custom successors have 47 focuses.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `CFR`: 47 focuses, lines 19-1045.
  - `OGB`: 23 focuses, lines 1048-1608.
  - `MFR`: 58 focuses, lines 1611-2994.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - `KZR`, `SOG`, `KHW`, `ALN`: 16 focuses each.

## Findings

### 1. Idea spam is not present directly in focus files, but reward helper spam is still real

Evidence:

- Direct `add_ideas`, `swap_ideas`, and `add_timed_idea` counts in the four focus files are currently zero.
- The focus-used helper definitions I checked in `common/scripted_effects/005_soviet_collapse_effects.txt` also did not directly call `add_ideas`, `swap_ideas`, or `add_timed_idea`.
- The remaining direct idea grants in `common/scripted_effects/005_soviet_collapse_effects.txt` appear to be startup/load/evolution effects, not focus rewards, for example `add_ideas = soviet_collapse_republican_startup_disorder` at line 4212 and custom successor startup grants around lines 18450-19081.

The user complaint still partially holds because the focus reward layer heavily repeats the same broad helper effects:

- `soviet_collapse_apply_focus_depot_and_supply_control` is called 142 times from focus files; first seen at `005_soviet_collapse_republics.txt:113`.
- `soviet_collapse_apply_focus_military_consolidation` is called 131 times; first seen at `005_soviet_collapse_republics.txt:564`.
- `soviet_collapse_apply_focus_legal_recognition` is called 108 times; first seen at `005_soviet_collapse_republics.txt:88`.
- `soviet_collapse_apply_focus_republican_compact_plan` is called 92 times; first seen at `005_soviet_collapse_republics.txt:2868`.
- `soviet_collapse_apply_focus_foreign_channel` is called 66 times; first seen at `005_soviet_collapse_republics.txt:246`.

These helpers are not empty, but they are broad catch-all payloads. For example, `soviet_collapse_apply_focus_legal_recognition` at `common/scripted_effects/005_soviet_collapse_effects.txt:9155-9172`, `soviet_collapse_apply_focus_military_consolidation` at lines 9255-9274, and `soviet_collapse_apply_focus_depot_and_supply_control` at lines 9276-9293 all add generic depth/progress pressure plus route payloads. This keeps rewards functional but makes many focuses feel same-shaped unless the focus adds a strong bespoke effect beside the helper.

### 2. High-chaos aggression is partly fixed, but it is too centralized and uneven

The system now has a strong generic high-chaos payload:

- `soviet_collapse_apply_high_chaos_focus_payload` at `common/scripted_effects/005_soviet_collapse_effects.txt:9174-9233` can add conquer/antagonize AI strategies against SOV at lines 9195-9197 and can declare war at chaos tier 5 or terminal-collapse conditions at lines 9203-9221.
- Many generic focus helpers call that payload, including legal, socialist, military, and depot helpers at lines 9163, 9244, 9263, and 9284.

This means high-chaos successors may be more aggressive than the focus file alone suggests. The problem is that aggression is hidden behind generic helper calls and applies broadly whenever `has_country_flag = soviet_collapse_high_chaos_successor`, instead of being expressed as clear route-specific payoffs. That makes individual focus rewards hard to reason about and can make different chaos countries feel mechanically similar.

Direct aggressive examples that are good but uneven:

- `DSC_congress_of_the_dead_army` declares war on SOV if possible and adds conquer/antagonize AI strategy at `005_soviet_collapse_custom_splinters.txt:3479-3501`.
- `TSC_starfall_mandate` creates a wargoal and adds conquer/antagonize AI strategy but does not directly declare war at `005_soviet_collapse_custom_splinters.txt:2458-2479`.
- `KZR_expansionist_steppe_levy` creates a wargoal, adds AI strategy, spawns assault columns, and applies neighbor expansion helpers at `005_soviet_collapse_ancient_restorations.txt:248-279`.
- `OGB_the_old_name_survives_modern_war` creates a wargoal at `005_soviet_collapse_factory_successors.txt:1575-1584` and continues with endgame handling after that range.

Weak or still restrained examples:

- Ukraine’s high-chaos line has several `ai_will_do` bases of only 2 and mostly generic helper/stat rewards: `ukr_soviet_collapse_bread_state_whispers` at `005_soviet_collapse_republics.txt:2075-2105`, `ukr_soviet_collapse_dead_fields_living_columns` at lines 2137-2161, `ukr_soviet_collapse_no_one_leaves_the_bread_line` at lines 2186-2203, and `ukr_soviet_collapse_last_harvest_plan` at lines 2207-2223. These do not visibly create decisive wargoals, annexation claims, forced conflicts, or OP unit/map payloads in the focus file.
- Kazakhstan’s capstone `kaz_soviet_collapse_the_steppe_outlives_the_union` is broad but defensive/recognition-oriented: it requires many completed routes at lines 12154-12166 and rewards mostly republican/depot helper payloads plus political power at lines 12168-12176. For a user wanting OP/aggressive chaos behavior, this is not a strong payoff.
- Route-specific external AI strategy exists for UKR/BLR/KAZ in `common/ai_strategy/005_soviet_collapse.txt:268-716`, but most strategies are build/supply/avoid-war support. Ukraine expansion and black-banner routes get army/supply values at lines 379-434, but no route-level conquer/invade strategy there. Belarus national and foreign routes explicitly include `avoid_starting_wars` at lines 452-456 and 536-537.

### 3. Ukraine is broad and no longer branchless, but high-chaos/pathline clutter remains

Positive evidence:

- Ukraine has explicit shortcuts for political, industry, and expansion at `005_soviet_collapse_republics.txt:34-47`.
- It has clear political locks around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_elections_under_shellfire` at lines 257-340.
- It has direct expansion nodes such as `ukr_soviet_collapse_direct_national_claims` at line 1740 and `ukr_soviet_collapse_great_steppe_and_sea_plan` at line 1911.

Remaining problems:

- The route-lock area has duplicated comments and asymmetric visual mutual exclusions at lines 254-331. `ukr_soviet_collapse_elections_under_shellfire` only mutually excludes the socialist route at line 331, while black-banner excludes socialist/officers at lines 296-299. The hidden route-completed trigger may prevent actual multi-route completion, but the visible pathline/mutual-exclusion graph remains uneven.
- The high-chaos/bread-state cluster is visibly mis-indented and has repeated role comments at lines 2021-2320. Syntax balances, but the visual layout is noisy.
- Ukraine high-chaos AI bases are mostly 2, and rewards lean on generic helper effects rather than decisive aggression, as listed above.

Priority: keep Ukraine’s expanded structure, but clean the high-chaos lane into a readable fork with explicit final payoffs and route-specific AI aggression. This should be a bounded design pass, not bulk regeneration.

### 4. Belarus has distinct rail/forest/corridor themes, but gate logic and route lock display are still cluttered

Positive evidence:

- Belarus has clear opening survival lanes and a central route question at `blr_soviet_collapse_which_road_is_belarus`, lines 8922-8960.
- It has visible rail, forest, military, foreign-corridor, and league/depot lanes through the later tree, including rail nodes around lines 9245-9495 and forest nodes around lines 9516-9740.

Remaining problems:

- `blr_soviet_collapse_which_road_is_belarus` uses one prerequisite block with all three opening focuses at lines 8928-8932, then an `available` OR-of-two-of-three workaround at lines 8933-8948. This is valid but pathline and tooltip-heavy.
- The four route locks at lines 9006-9115 use mixed pairwise mutual exclusions plus a hidden route-completed trigger. The visual mutex graph is asymmetric:
  - National Council excludes Socialist only at line 9013.
  - Socialist excludes National Council and Military at lines 9041-9044.
  - Military excludes Socialist and Foreign at lines 9070-9072.
  - Foreign excludes Military only at line 9103.
- This likely works because of `has_soviet_collapse_belarus_state_route_completed`, but the visible graph still looks inconsistent and can support the user’s pathline-clutter complaint.

Priority: replace the visual route lock clutter with a cleaner four-route hub pattern if the parent wants a gameplay pass. If keeping hidden route completion as the enforcement mechanism, reduce mutual exclusions to the minimum needed for pathline clarity.

### 5. Kazakhstan is large and branch-rich, but its gates are dense and its endpoint is not aggressive

Positive evidence:

- Kazakhstan has shortcuts for political, industry, and expansion at `005_soviet_collapse_republics.txt:10161-10175`.
- It has 92 focuses, with political, resource, military, southern federation, Alash, socialist, industry, and foreign lanes.

Remaining problems:

- `kaz_soviet_collapse_the_congress_chooses_a_past` repeats the same two-of-three gate pattern as Belarus: all three focuses in prerequisites at lines 10256-10260, then OR combinations in `available` at lines 10261-10276.
- `kaz_soviet_collapse_steppe_federation_charter` uses a dense six-case OR gate plus war/threat gate at lines 10826-10858.
- `kaz_soviet_collapse_lone_steppe_state` hides its rivalry with the federation route through `available` rather than a visual mutex at lines 10880-10886.
- The capstone `kaz_soviet_collapse_the_steppe_outlives_the_union` requires a very long checklist at lines 12154-12166 and rewards mostly broad helper payloads at lines 12168-12176. It reads as a completion audit node more than a punchy final play payoff.

Priority: keep the current depth, but simplify the visible gates. Add one or two aggressive/OP payoffs to the federation/resource/steppe endgame instead of only recognition/depot helper rewards.

### 6. Several custom/splinter trees still feel compact or template-shaped

The custom/splinter file has improved a lot, but it is uneven:

- `PRA` has 22 focuses and `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` have only 18 each. These are better than stubs, but still too compact for “major chaos country” expectations.
- `TSC_soviet_collapse_focus_tree` at `005_soviet_collapse_custom_splinters.txt:2022-2529` has a compact political/industry/military/league/chaos spread, but the “industry” lane is mostly a handful of station/radar/train rewards at lines 2081-2187 and does not become a full branch.
- `DSC_soviet_collapse_focus_tree` at lines 3010-3547 has strong aggression in the opening and endgame, but still has several reward blocks that are just accumulated variables/helpers, and several indentation/layout inconsistencies around lines 3183-3213, 3260-3305, 3405-3412, and 3479-3502.
- The later 47-focus custom trees use a recognizable repeated skeleton: `birth`, `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `war_plan`, `diplomatic_plan`, `industry_plan`, `hidden_doctrine`, `extreme_gate`, `endgame`, `extreme_path`. BSC shows this at lines 4542-4758, and the same skeleton recurs for TNC/ALA/BBH/KRS/UDC/SDZ and later trees.

Priority: do not bulk-regenerate. Pick the weakest short trees first (`TSC`, `RMC`, `NRF`, `ICD`, then `PRA`) and add bespoke branches/endgame rewards. For the 47-focus template trees, preserve the branch count but replace repeated generic helper-only nodes with country-specific payoffs, route locks, and AI strategy.

### 7. Ancient restoration trees are compact and helper-only in places

The four ancient restoration trees are only 16 focuses each. They have a useful symbolic-vs-expansionist fork, but they do not meet the full political/industrial/expansion branch standard if treated as major playable chaos countries.

Evidence:

- `KZR_symbolic_crossing_state` and `KZR_expansionist_steppe_levy` form a clear fork at `005_soviet_collapse_ancient_restorations.txt:212-285`.
- The KZR end of tree runs to line 421, then SOG begins at line 424.
- The mechanical parse found eight helper-only rewards in each ancient tree. These are not necessarily broken, but they make the compact trees feel less bespoke.

Priority: if ancient restorations are intended as compact side-country packages, current scope is acceptable with known simplification. If they are intended to satisfy “chaos countries should be OP/aggressive,” they need larger route families and clearer war/claim/faction/AI end states.

## Validation Run

Commands run:

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus|Focus'`
- Read required offline wiki pages and vanilla docs listed above.
- `wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Structural parse of four focus files:
  - 1,698 focus ids found.
  - 2,589 checked focus references in prerequisites, mutual exclusions, relative positions, and `has_completed_focus`.
  - 0 missing checked focus references.
  - 0 brace-balance errors.
- Reward/helper scan:
  - 0 direct `add_ideas`, `swap_ideas`, or `add_timed_idea` calls in the four focus files.
  - 280 distinct `soviet_collapse_* = yes` helpers called by focus files, 1,988 total mentions.
- `git diff --stat -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Existing parent worktree changes before this audit: 4 files changed, 4,647 insertions, 4,466 deletions.

Skipped validation:

- I did not run the game.
- I did not edit or validate localisation, assets, flags, or interface files because this task explicitly scoped the audit to current focus-tree state and forbade flag/interface touches.

## Prioritized Remaining Fixes

1. Clean Ukraine high-chaos path:
   - Normalize indentation/role comments around `ukr_soviet_collapse_bread_state_whispers` through `ukr_soviet_collapse_last_harvest_plan`.
   - Raise or contextualize AI desire for black-banner/bread-state aggression.
   - Add explicit war/claim/unit/map payoffs where the final branch currently only calls generic helpers.

2. Simplify Belarus route-lock display:
   - Replace mixed pairwise mutual exclusions with a clearer visual hub or consistent pairwise pattern.
   - Preserve the hidden route-completed enforcement if it is still needed.

3. Simplify Kazakhstan gates:
   - Rework two-of-three and six-case `available` gates into cleaner branch unlocks or helper triggers.
   - Make the capstone a real strategic payoff, not only a checklist completion node.

4. Reduce repeated helper reward feel:
   - Keep shared helpers for baseline variables and pressure.
   - Add bespoke visible rewards on focuses that currently only feel like `set_country_flag + generic helper`.
   - Consider small route-specific scripted helpers for repeated country families instead of one huge catch-all helper path.

5. Target short custom/splinter trees first:
   - Expand or deepen `TSC`, `RMC`, `NRF`, `ICD`, then `PRA`.
   - Keep `DSC` aggression but clean indentation and make the non-war branch as distinctive as the war branch.

6. Decide ancient restoration scope:
   - If compact side trees are acceptable, document them as intentional compact packages.
   - If they must satisfy the same “OP/aggressive chaos country” standard, add real political/industrial/diplomatic/expansion branch families and stronger endgame AI.

## Completion Honesty

This audit does not prove Event005 focus trees are complete. It proves the current focus files are syntactically brace-balanced, focus references are internally consistent by mechanical scan, and direct focus-file idea spam is not present. The user’s complaints remain partially valid for repeated helper rewards, cluttered route gates, uneven aggression, and compact/template-shaped custom trees.
