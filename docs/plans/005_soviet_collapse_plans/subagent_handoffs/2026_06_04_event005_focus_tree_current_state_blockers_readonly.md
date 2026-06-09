# Event005 Focus Tree Current-State Blockers Audit

Date: 2026-06-04

Role: `chaosx_focus_tree_auditor`

## Scope and Constraints

Audited the current Event005 Soviet Collapse focus trees in:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Used repo skills:

- `hoi4-focus-trees`
- `chaos-redux-subagents`

Required references consulted before inspecting the Chaos Redux focus files:

- `AGENTS.md`
- Offline Paradox wiki core pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Offline Paradox wiki `National focus modding - Hearts of Iron 4 Wiki.md`
- Vanilla documentation in `~/projects/Hearts of Iron IV/documentation/`, including effects, triggers, modifiers, localisation objects, and script concepts
- Vanilla focus files list and focus syntax precedent in `~/projects/Hearts of Iron IV/common/national_focus/`

Critical invariant honored: **DO NOT TOUCH FLAGS.** I did not edit `gfx/flags`, `.tga`, flag sprites, flag `.gfx`, or visual flag assets. No patches were made to gameplay or asset files in this audit.

## Summary

No focus-file patch was made. The current four focus files no longer show the earlier worst direct idea-spam surface: there are no direct `add_ideas`, `swap_ideas`, or `remove_ideas` calls in the inspected focus rewards. The hard structural scan also found no duplicate focus IDs, no duplicate coordinates, and no missing prerequisite or mutual-exclusion targets across 1,698 focuses.

The remaining blockers are mainly design-state blockers: custom chaos-country trees still lean too much on generic helper payloads, most 47-focus chaos splinter trees do not directly produce aggressive map pressure or postwar handling, several political routes lack visible country-identity consequences on the focus surface, and some major/republic layouts still place unrelated or branching focuses only one grid column apart.

## Audit Counts

- Total focuses: 1,698
- Total trees: 41
- `005_soviet_collapse_republics.txt`: 501 focuses
- `005_soviet_collapse_custom_splinters.txt`: 1,005 focuses
- `005_soviet_collapse_factory_successors.txt`: 128 focuses
- `005_soviet_collapse_ancient_restorations.txt`: 64 focuses
- Duplicate focus IDs: 0
- Duplicate coordinates inside a tree: 0
- Missing prerequisite or mutual-exclusion references: 0
- Missing `ai_will_do`: 0
- Direct focus reward `add_ideas` / `swap_ideas` / `remove_ideas`: 0

## Ranked Blockers

1. **Most custom chaos splinter trees are still not aggressive enough on the focus surface.**

   The 25 custom chaos splinter trees contain 1,005 focuses, but only 6 direct `create_wargoal` calls and 0 direct `add_state_claim` calls in the file-level scan. Many trees have only helper-driven or implied expansion. Example: `NLC_extreme_gate` at `005_soviet_collapse_custom_splinters.txt:25371` spawns assault columns and calls `soviet_collapse_apply_custom_splinter_expansion_claims` at lines 25395-25397, but does not directly create a war goal or define postwar settlement. This can still be valid if the helper is strong, but the current focus surface does not prove the chaos-country trees are as openly aggressive as the requested end state.

2. **Generic helper identity rewards still carry too much of the route meaning.**

   Several early custom-splinter focuses resolve into generic tooltip plus hidden helper calls instead of country-specific visible consequences. Example: `FTH_first_guard` uses `soviet_collapse_custom_splinter_military_route_reward_tt` and `soviet_collapse_apply_custom_splinter_first_guard_identity` at `005_soviet_collapse_custom_splinters.txt:61-67`; `FTH_stores` does the same pattern for logistics at lines 85-90. This avoids raw idea spam, but it still risks shallow/random rewards if the helper does not create distinct country mechanics, decisions, or route-specific consequences.

3. **Many 47-focus custom splinter trees have no direct decision unlocks or event payoffs.**

   Tree-level scan found 0 `unlock_decision_tooltip` and 0 event/news/super-event calls in many 47-focus custom splinters, including `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, and `NLC`. Example: the `BSC` mid-tree has diplomacy/logistics content at `005_soviet_collapse_custom_splinters.txt:4714-4994`, but no direct decision unlocks or event payoffs in that tree. The result is branch depth that often changes variables/buildings rather than opening new play.

4. **Visible political transformation is thin in the focus files themselves.**

   A scan for direct visible country-identity effects found only one direct `set_cosmetic_tag` call in the four focus files, at `005_soviet_collapse_republics.txt:296`, and a small number of `add_popularity` calls in `005_soviet_collapse_factory_successors.txt` such as `CFR_the_concrete_committee` at lines 246-249. There are no direct `set_politics`, `set_ruling_party`, `load_focus_tree`, or direct leader/advisor changes in the focus files. Some of this may be hidden in scripted helpers, but the focus surface alone does not prove the political branches create enough visible state identity.

5. **Layout crowding remains in several major and regional trees.**

   There are no duplicate coordinates, but at least 19 same-row adjacent focus pairs remain with only one x-column of separation. Examples:

   - `ukr_soviet_collapse_war_without_a_declaration` at `005_soviet_collapse_republics.txt:164` sits one column from `ukr_soviet_collapse_army_of_the_republic` at line 1112.
   - `ukr_soviet_collapse_british_caution` at `005_soviet_collapse_republics.txt:1380` sits between adjacent same-row focuses at lines 593 and 1208.
   - `kaz_soviet_collapse_no_concession_without_a_republic`, `kaz_soviet_collapse_the_steppe_arsenal`, and `kaz_soviet_collapse_the_resource_towns_demand_seats` sit at same-row adjacent x positions around `005_soviet_collapse_republics.txt:10470`, `10781`, and `11010`.
   - `FTH_supply` and `FTH_enemy_front` are adjacent at `005_soviet_collapse_custom_splinters.txt:283` and line 306.

   These are not syntax errors, but they directly support the user's complaint that some focuses are too close together and likely make pathlines harder to read.

6. **OR prerequisites after mutually exclusive choices are valid but still create pathline-risk candidates.**

   Some convergence focuses intentionally accept either mutually exclusive route. This is valid HOI4 syntax, but it can create cluttered visual lines if the convergence is not centered or if siblings are dense. Examples:

   - `KZR_khazar_charter` converges from `KZR_symbolic_crossing_state` or `KZR_expansionist_steppe_levy` at `005_soviet_collapse_ancient_restorations.txt:283-290`.
   - `CFR_apartment_blocks_for_loyalty` converges from `CFR_cities_first` or `CFR_rails_first` at `005_soviet_collapse_factory_successors.txt:497-503`.
   - `ukr_soviet_collapse_last_harvest_plan` converges from three high-chaos route endpoints at `005_soviet_collapse_republics.txt:2190-2197`.

   I did not patch these because the hard references are valid and prior handoffs already patched the clearest CFR mutual-exclusion display mismatch. Remaining changes need visual/layout review, not a blind coordinate move.

7. **Some compact trees are structurally coherent but still below major-country depth expectations.**

   Ancient restorations have 16 focuses each and compact TSC/RMC/DSC/NRF/ICD trees have 18 focuses each. The ancient trees have strong direct claims/wargoals, e.g. `KZR_expansionist_steppe_levy` at `005_soviet_collapse_ancient_restorations.txt:236-280` and `SOG_expansionist_merchant_claims` at lines 629-673. However, compact trees still have limited internal faction, diplomacy, industry/logistics, and late-game depth compared to the focus-tree skill's standard for playable event-created countries.

## Route-Depth Coverage Table

| Tree family | Political | Industry/logistics | Military | Diplomacy | Expansion | Special mechanic | Endgame | Current status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bespoke republic majors (`UKR`, `BLR`, `KAZ`, `MOL`) | Strong count, but identity often helper-based | Present | Present | Present | Thin relative to tree size | Strong variable/helper integration | Present but uneven | Needs layout spacing and more visible route payoffs |
| Shared/region republic trees | Present | Present | Present | Present | Moderate in Baltic/Caucasus/Central Asia, weaker elsewhere | Strong variable/helper integration | Thin | Needs more branch-specific end states and decision unlocks |
| Custom chaos splinters | Present by count | Present by count | Present by count | Mixed | Too weak/directly sparse for chaos tags | Strong helper/variable integration | Present but often generic | Highest priority for aggression, claims/wars, and postwar handling |
| Factory/death successors | Strong for CFR/PRA, compact for death tags | Strongest family for industry | Mixed | Mixed | Sparse outside a few aggressive endpoints | Strong | Present | CFR is deepest; compact death tags need route depth if meant playable |
| Ancient restorations | Present | Present | Present | Present | Strong for 16-focus trees | Strong local authority variables | Present | Structurally coherent, but compact and should gain more postwar/settlement depth if elevated |

## Safe Patches Made

None.

I did not patch because the current hard-structure scan found no duplicate IDs, no missing refs, no missing AI blocks, no direct idea-spam reward, and no single obvious local route-lock error that would materially advance the user's requested final state. The remaining issues require parent-level design and likely touch scripted effects, decisions, ideas, localisation, and possibly focus layout across many trees. Those surfaces were explicitly out of this subagent's small-patch scope.

## Parent Follow-Up Recommendations

1. Prioritize a custom chaos splinter aggression pass. For each 47-focus chaos tree, add a distinct expansion branch endpoint with direct claims or wargoal path, postwar settlement handling, AI strategy, and decision/event consequences. Do not rely only on shared helper names unless the helper is visibly country-specific.

2. Convert generic helper payloads into route-specific play. Keep the existing helpers where they centralize mechanic values, but add tree-specific decisions, missions, events, postwar handling, or scripted GUI/status text so military, industry, diplomacy, and radical branches play differently.

3. Add direct route payoff proof to political branches. The parent should inspect the helper implementations and ensure political routes visibly change ruling party, leader/council/advisors, cosmetic identity, route mechanics, or decision categories where appropriate. Do not change flags unless the user explicitly reopens flag scope.

4. Run a visual layout pass on adjacent same-row pairs and OR-convergence nodes. Start with Ukraine, Kazakhstan, Belarus, Moldova, and the FTH/BSC/NLC custom splinter layouts. Move focus coordinates only after checking pathlines in-game or with a layout visualization, because the references are mostly valid and blind moves risk new crossings.

5. Expand compact death-state and ancient-restoration trees only if they are intended to be playable majors. Ancient restorations already have direct claims and wargoals, so the next gain is not more aggression alone; it is deeper settlement, legitimacy, diplomacy, integration, and late-game route identity.

6. Keep the no-flag invariant until the parent/user explicitly changes it. If a route identity normally calls for a flag or cosmetic flag, document the asset need instead of editing flag files.

## Validation Run

Passed/read-only checks:

- Parsed all four scoped focus files and extracted 1,698 focus blocks.
- Duplicate focus IDs: 0.
- Duplicate coordinates within each tree: 0.
- Missing prerequisite/mutual-exclusion targets: 0.
- Missing `ai_will_do`: 0.
- Direct `add_ideas`, `swap_ideas`, `remove_ideas` in inspected focus files: 0.
- Unsupported less-or-equal / greater-or-equal operator scan on the four inspected focus files returned no matches; no new operators were added.
- No gameplay focus-file patch was made.

Flag diff guard:

- `git status --porcelain=v1 | rg "(^.. gfx/flags/|^.. .*\\.tga$|flag|flags|interface/.*flag.*\\.gfx|\\.gfx$.*flag)"` returned only pre-existing Event006 achievement/icon paths with `flags` in their names, not `gfx/flags`, `.tga`, flag sprites, flag `.gfx`, or Event005 flag assets.
- `git diff --name-only -- ... gfx/flags interface` showed the four focus files and unrelated interface files already dirty in the worktree; no `gfx/flags` path appeared.

Skipped:

- No game launch or live in-game verification. This is a subagent audit handoff; parent owns final integration validation.
- No scripted helper, decision, idea, localisation, or asset edits were made.
