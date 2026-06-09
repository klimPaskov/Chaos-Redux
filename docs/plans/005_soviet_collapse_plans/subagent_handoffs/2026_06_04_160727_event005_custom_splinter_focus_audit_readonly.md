# Event005 Custom Splinter Focus Audit Handoff

Audit mode: read-only. No focus, localisation, interface, `gfx/flags`, or `interface/flags` files were edited.

## Scope

Priority file:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Secondary files sampled for comparison and remaining blockers:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

Reference material opened before audit:

- `.agents/skills/hoi4-focus-trees/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`
- Vanilla focus precedents sampled from `generic.txt`, `finland.txt`, `france.txt`, and `germany.txt`

## Current-State Summary

- Parsed 1698 focuses across the four Event005 focus files.
- No duplicate focus IDs found across the four Event005 focus files.
- No direct focus-level `add_ideas`, `add_timed_idea`, `swap_ideas`, `modify_idea`, or `remove_ideas` calls found in the four Event005 focus files.
- FTH and SDZ are materially improved from the older audit state. FTH still has five `soviet_collapse_custom_splinter_payoff` helper references, but no generic route-tooltip keys; SDZ has no remaining generic custom-splinter helper references in its focus tree.
- UDC is only partially improved: ten generic custom-splinter route tooltip/helper references remain in the current file.
- Corrected coordinate audit found no current custom-splinter duplicate-coordinate or one-step same-row spacing issues. Remaining concrete pathline/layout risks are in republic trees, not the custom-splinter file.
- `soviet_collapse_apply_high_chaos_focus_identity_payload` now excludes both red-martyr and iron-commissariat successors from the generic fallback block, so the older high-chaos double-apply finding appears fixed.

## Findings Ordered By Severity

### 1. Many 47-focus custom splinters still have no real route mechanics

Severity: high.

The biggest remaining blocker is no longer FTH/SDZ. It is the untouched or only-lightly-touched 47-focus custom-splinter trees that still have little to no decision, map/war, or route-specific AI surface in the focus file.

Worst current cases:

- `BBH_soviet_collapse_focus_tree` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:7726`: 47 focuses, 22 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `KRS_soviet_collapse_focus_tree` at line 8921: 47 focuses, 20 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `GAC_soviet_collapse_focus_tree` at line 12615: 47 focuses, 22 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `DHC_soviet_collapse_focus_tree` at line 13785: 47 focuses, 20 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `KHC_soviet_collapse_focus_tree` at line 14984: 47 focuses, 20 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `FEV_soviet_collapse_focus_tree` at line 16173: 47 focuses, 24 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `SZA_soviet_collapse_focus_tree` at line 17341: 47 focuses, 21 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `UWD_soviet_collapse_focus_tree` at line 18505: 47 focuses, 22 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `MRC_soviet_collapse_focus_tree` at line 19692: 47 focuses, 21 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `IUL_soviet_collapse_focus_tree` at line 20865: 47 focuses, 20 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.
- `BAC_soviet_collapse_focus_tree` at line 22005: 47 focuses, 21 generic helper references, 0 decision focuses, 0 map/war focuses, 0 `add_ai_strategy` focuses.

Patch direction: do one tree at a time. For each tree, replace generic route-helper focuses with identity-specific tooltips plus at least one concrete mechanic per branch family: decision unlocks, claims/cores/war plans, units/equipment, construction packages, route variables, and route-specific AI strategies.

### 2. UDC still contradicts the recent UDC completion claim

Severity: high.

The current file still contains ten UDC generic helper/tooltips:

- `UDC_doctrine` at `common/national_focus/005_soviet_collapse_custom_splinters.txt:10279`
- `UDC_economy` at line 10302
- `UDC_league` at line 10325
- `UDC_foreign` at line 10348
- `UDC_diplomatic_plan` at line 10371
- `UDC_inner_faction` at line 10396
- `UDC_special_arm` at line 10420
- `UDC_command_bunker_vaults` at line 10779
- `UDC_settlement` at line 11138
- `UDC_extreme_gate` at line 11273

This is not safe for a blind token patch because the matching `UDC_*_tt` localisation keys do not exist for most of these route nodes. The next parent tranche should add UDC-specific localisation and mechanic-facing hidden effects for those exact focuses, similar to the existing `UDC_first_guard_tt`, `UDC_stores_tt`, `UDC_legitimacy_tt`, `UDC_rival_tt`, `UDC_supply_tt`, `UDC_enemy_front_tt`, `UDC_war_plan_tt`, `UDC_civil_rule_tt`, `UDC_propaganda_tt`, `UDC_signal_truck_yards_tt`, `UDC_industry_plan_tt`, and `UDC_hidden_doctrine_tt`.

### 3. Generic helper references remain concentrated in untouched route scaffolds

Severity: high.

Highest generic-reference counts in `005_soviet_collapse_custom_splinters.txt`:

- `NLC_soviet_collapse_focus_tree`: 29 generic helper references.
- `BSC_soviet_collapse_focus_tree`: 24 generic helper references.
- `FEV_soviet_collapse_focus_tree`: 24 generic helper references.
- `ARD_soviet_collapse_focus_tree`: 24 generic helper references.
- `ALA_soviet_collapse_focus_tree`: 22 generic helper references.
- `BBH_soviet_collapse_focus_tree`: 22 generic helper references.
- `GAC_soviet_collapse_focus_tree`: 22 generic helper references.
- `UWD_soviet_collapse_focus_tree`: 22 generic helper references.

Typical repeated nodes are `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `inner_faction`, `special_arm`, `supply`, `enemy_front`, `war_plan`, `civil_rule`, `propaganda`, `settlement`, `industry_plan`, `hidden_doctrine`, and `extreme_gate`.

Patch direction: the parent should prioritize NLC, BSC, FEV, and ARD after UDC because they have the densest remaining generic scaffold.

### 4. Idea spam is not focus-level now, but helper-side lifecycle risk remains

Severity: medium.

The four Event005 focus files no longer directly add, remove, swap, or modify ideas from focus rewards. That part of the old idea-spam problem appears cleared in the focus files.

Remaining risk is helper-side and route-design-side:

- Many route focuses still call generic identity helpers, so the player-facing effect may still feel like repeated national-spirit progression even when the actual `add_ideas` is hidden in scripted effects.
- Major staged helpers should keep one idea family per institution and update it through documented scripted effects. Avoid creating new per-focus national spirits as the next trees are deepened.

### 5. Republic-tree pathline risks remain outside the custom-splinter tranche

Severity: medium.

Corrected coordinate audit found the remaining concrete layout/pathline issues in `common/national_focus/005_soviet_collapse_republics.txt`:

- Ukraine: `ukr_soviet_collapse_breadbasket_empire` at line 1777 is a prerequisite for `ukr_soviet_collapse_bread_state_whispers` at line 2051, but the child sits at the same y-layer `(19,9)` instead of below the prerequisite `(24,9)`. This can create bad pathline behavior.
- Ukraine same-row crowding remains around diplomacy/naval and socialist/military lanes, including lines 210/1204, 333/805, 351/639, 481/1998, and 481/2204.
- Central Asia: `central_asia_soviet_collapse_khwarazm_restoration_debate` at line 7374 is a prerequisite for `central_asia_soviet_collapse_the_southern_shield` at line 7183 while both sit on y 8. Same-row crowding also remains at lines 6810/7326, 6892/7374, and 7067/7153.
- Moldova: the vertical path from `moldova_soviet_collapse_river_guard_brigades` line 7759 to `moldova_soviet_collapse_the_river_state` line 8630 passes through `moldova_soviet_collapse_tiraspol_depot_belt` line 8417 on the same x lane.

No custom-splinter coordinate patch is recommended from this audit; the custom layout problems appear resolved enough for the current tranche.

### 6. Republic focus files still trail the chaos-country standard

Severity: medium.

Secondary sampling still shows republic trees with too little map/war and route AI payload:

- `soviet_collapse_breakaway_focus_tree` at `common/national_focus/005_soviet_collapse_republics.txt:2308`: 36 focuses, 0 decision focuses, 0 map/war focuses, 0 route-specific AI strategy focuses.
- `soviet_collapse_internal_republic_focus_tree` at line 3099: 62 focuses, 0 decision focuses, 1 map/war focus, 0 route-specific AI strategy focuses.
- `soviet_collapse_baltic_focus_tree` at line 4565: 42 focuses, 0 decision focuses, 0 map/war focuses, 0 route-specific AI strategy focuses.
- `soviet_collapse_moldova_focus_tree` at line 7552: 48 focuses, 0 decision focuses, 0 map/war focuses, 0 route-specific AI strategy focuses.
- `soviet_collapse_kazakhstan_focus_tree` at line 10004: 92 focuses, 4 decision focuses, 0 map/war focuses, 0 route-specific AI strategy focuses.

These are not the current parent priority file, but they remain blockers for the overall Soviet Collapse focus-tree goal.

## Recommended Next Tranches

1. Finish UDC cleanup first because it was recently reported as improved but still has ten current generic route nodes.
2. Deepen NLC or BSC next. They have the highest generic-helper density and still lack route-specific AI/map payloads.
3. Continue one-tree custom-splinter tranches in this order unless the parent has a newer priority: NLC, BSC, FEV, ARD, ALA, BBH, GAC, UWD, MRC, IUL, BAC, KRS, DHC, KHC, SZA, TNC.
4. After the custom-splinter pass, run a republic layout tranche for Ukraine, Central Asia, and Moldova pathlines.

## Validation

Read-only audit validation run:

- Python parser over the four Event005 focus files for focus-tree counts, duplicate focus IDs, direct idea effects, generic custom-splinter helper references, decision/map/AI/building/unit reward counts, and corrected coordinate/pathline checks.
- Unsupported comparison-operator grep should still be run by any patching agent on touched files. This audit did not patch focus or localisation files.
- `git diff --check` should still be run by any patching agent on touched files. This audit only adds this markdown handoff.

Skipped validation:

- No localisation BOM check was required because no localisation files were touched.
- No in-game validation was run.

## Changed Files

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_160727_event005_custom_splinter_focus_audit_readonly.md`

## Simplifications, Omissions, And Blockers

- No gameplay patch was made. This is a read-only audit handoff only.
- Republic files were sampled after the custom-splinter priority audit; this is not a full republic rewrite plan.
- No flag assets were inspected or edited.
