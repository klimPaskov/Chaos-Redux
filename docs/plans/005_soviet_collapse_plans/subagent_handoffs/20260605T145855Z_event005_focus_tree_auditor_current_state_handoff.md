# Event005 Soviet Collapse focus-tree auditor handoff

Timestamp: 20260605T145855Z
Agent role: chaosx_focus_tree_auditor

## Scope

Audited current-state focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Explicitly did not touch `gfx/flags` or flag sprite files.

Required references read before opening/editing focus files:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/common/focus_inlay_windows/documentation.md`
- Vanilla focus precedent: `/home/klim/projects/Hearts of Iron IV/common/national_focus/china_nationalist.txt`

## Files changed

Changed only:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed identifiers:

- `soviet_collapse_belarus_focus_tree`
- `blr_soviet_collapse_prepare_league_freight_tables`

No helper, scripted trigger, script constant, localisation, gfx, flag, or flag sprite files were edited.

## Patch summary

1. Moved the Belarus continuous focus panel from `continuous_focus_position = { x = 3264 y = 180 }` to `continuous_focus_position = { x = 3648 y = 180 }`.
   - Reason: the Belarus tree reaches `x = 33`, whose focus pixel column is `3168`; the old panel position began at `3264`, leaving no practical clearance after the rightmost forest branch.
   - Current line: `common/national_focus/005_soviet_collapse_republics.txt:8820`.

2. Moved `blr_soviet_collapse_prepare_league_freight_tables` from `x = 17, y = 12` to `x = 17, y = 13`.
   - Reason: it exactly overlapped `blr_soviet_collapse_league_supply_timetables` at `x = 17, y = 12`.
   - Current lines: `blr_soviet_collapse_league_supply_timetables` at `common/national_focus/005_soviet_collapse_republics.txt:9343`; `blr_soviet_collapse_prepare_league_freight_tables` at `common/national_focus/005_soviet_collapse_republics.txt:9765`.

The patch is bounded because it changes only layout coordinates and does not alter prerequisites, rewards, route gates, effects, AI, or localisation.

## Validation performed

Mechanical focus audit across all four named files:

- Parsed `41` focus trees.
- Parsed `1698` focus blocks.
- Found `0` duplicate focus IDs.
- Found `0` exact coordinate overlaps after the patch.
- Found `0` missing required basics among parsed focuses: id, icon, x/y, search filters, completion reward, and ai_will_do.
- Found `0` prerequisite pathline violations where a parent focus is at or below its child.
- Found `0` continuous-panel clearance risks after the Belarus panel move.
- Confirmed there are no direct `add_ideas`, `add_idea`, or `add_timed_idea` calls in the four audited focus files.

Validation commands used included mechanical parsers over the four focus files plus targeted `rg`/`nl` checks around Belarus and route-lock blocks.

Skipped validation:

- No game launch or in-game focus-tree rendering was performed in this subagent pass.
- No helper body audit was performed beyond focus-file call-site frequency, because the prompt asked to keep this pass disjoint from parent scripted_effects/triggers/constants work.

## Current-state audit findings

### P0 - Ukraine and Belarus route locks are not real mutually exclusive route locks

Ukraine has route-choice focuses marked or functioning as route locks but no visible mutual exclusivity links among the main choices:

- `ukr_soviet_collapse_socialist_republic_without_moscow` at lines 258-274
- `ukr_soviet_collapse_black_banner_compact` at lines 282-304
- `ukr_soviet_collapse_elections_under_shellfire` at lines 310-326
- `ukr_soviet_collapse_officers_above_parties` at lines 530-552
- `ukr_soviet_collapse_protectorate_debate` later in the same tree

Only some later options use hidden `available` checks. The first three route focuses above do not mutually exclude each other and do not visibly communicate a route choice. This lets a player sequence multiple political routes unless downstream helpers block it invisibly.

Belarus has the same issue for the `blr_soviet_collapse_which_road_is_belarus` fork:

- `blr_soviet_collapse_national_council_of_minsk` at lines 8994-9015
- `blr_soviet_collapse_socialist_autonomy_without_moscow` at lines 9018-9037
- `blr_soviet_collapse_military_transit_directorate` at lines 9040-9063
- `blr_soviet_collapse_foreign_corridor_administration` at lines 9066-9088

Parent follow-up should add explicit mutual exclusions or reframe these as non-exclusive policy branches. If they remain route choices, use visible `mutually_exclusive` links plus clean route-specific availability/tooltips.

### P1 - Helper-mediated rewards are still heavily generic

The files no longer use direct idea spam, but many focuses still route rewards through the same broad helpers. Top repeated helpers across the audited files include:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 142 calls
- `soviet_collapse_apply_focus_military_consolidation`: 131 calls
- `soviet_collapse_apply_focus_legal_recognition`: 108 calls
- `soviet_collapse_apply_focus_republican_compact_plan`: 95 calls
- `soviet_collapse_apply_focus_foreign_channel`: 66 calls
- `soviet_collapse_apply_focus_security_supply_plan`: 65 calls
- `soviet_collapse_apply_focus_high_chaos_identity`: 54 calls
- `soviet_collapse_apply_focus_league_preparation`: 51 calls

This is better than visible idea spam, but the gameplay surface can still feel repetitive when distinct focus titles resolve to the same helper family. Parent should audit helper outputs and replace repeated generic helper-only rewards with country/route-specific unlocks, decisions, units, targets, or state/building effects where the focus concept is specific.

### P1 - Custom splinter templates remain recognizably cloned

The 47-focus high-chaos custom splinter trees share many identical suffixes across 19 tags:

- `birth`, `first_guard`, `stores`, `legitimacy`, `rival`, `doctrine`, `economy`, `league`, `foreign`, `inner_faction`, `special_arm`, `supply`, `enemy_front`, `civil_rule`, `propaganda`, `settlement`, `radical_turn`, `war_plan`, `diplomatic_plan`, `industry_plan`, `hidden_doctrine`, `extreme_gate`, `extreme_path`.

The later local branches improve identity, but the opening and route scaffold still reads as template-first. Parent should prioritize more bespoke opening forks for the highest-visibility tags instead of only varying late branch names and tooltips.

### P1 - Small high-chaos trees still need stronger OP/aggressive identity

The compact high-chaos/special trees with 16-23 focuses have usable branching, but several are not yet aggressive enough for their premise:

- `PRA_soviet_collapse_focus_tree`: 22 focuses; strong rail identity, but still leans on recognition/depot helpers early.
- `TSC`, `RMC`, `DSC`, `NRF`, `ICD`: 18 focuses each; they have concept-specific names and some high-chaos route hooks, but limited branch depth makes political/industrial/expansion play feel compressed.
- Ancient restorations (`KZR`, `SOG`, `KHW`, `ALN`): 16 focuses each; they do have symbolic vs expansionist mutual exclusions and direct wargoal/AI strategy payloads, but each tree uses the same compact architecture. Their expansion route is clearer than their internal politics or economy route.
- `OGB`: 23 focuses; clearer restoration choice structure, but its opening is still a narrow vertical legitimacy spine.

Parent should expand one or two high-impact special-country route families per tranche rather than adding more generic helper rewards.

### P2 - Ukraine layout is mechanically valid but still visually dense

Ukraine has no current exact coordinate overlaps and the continuous panel is clear, but it has 83 focuses spread across `x = 4..37`, `y = 0..20`. Several branches are packed around the same y-level route row, and the missing visible route mutex links make the layout harder to understand because route-choice nodes do not draw the expected red route-choice lines.

Parent should solve route locks first. After that, re-check pathline readability around the political route row and diplomacy/military lanes.

### P2 - Belarus layout is improved but the route row still needs logic cleanup

The specific overlap and continuous panel crowding are fixed. Belarus still has a broad route row at `y = 5` and several rail/forest follow-ups running close together from `y = 8..14`. The tree is now mechanically clean by coordinate and prerequisite checks, but route intent remains unclear until the route-choice focuses are mutually exclusive or explicitly made additive.

## Prioritized parent follow-up patches

1. Add or redesign visible route locks for Ukraine and Belarus.
   - Use `mutually_exclusive` for true route choices.
   - Keep availability tooltip text readable; do not hide all route logic in `hidden_trigger`.
   - Re-run pathline checks afterward because new red links can reveal between-node clutter.

2. Reward-depth tranche for helper-heavy generic rewards.
   - Start with the high-frequency helpers listed above.
   - Replace repeated helper-only rewards with route-specific decision unlocks, state targets, units, claims/settlement tools, AI strategies, or country-specific variables.

3. Custom splinter bespoke-opening tranche.
   - Pick the highest-played or most visible custom splinters first.
   - Replace cloned `birth/first_guard/stores/legitimacy/rival` openings with concept-specific openings that determine later political, military, industrial, and expansion branches.

4. Small high-chaos aggression tranche.
   - Prioritize PRA plus one of TSC/RMC/DSC/NRF/ICD.
   - Give each a stronger OP/aggressive payoff with visible war, expansion, or special-mechanic consequences.

5. Ancient restoration branch-depth tranche.
   - Keep their compact mutual-exclusion architecture, but deepen internal politics/economy beyond the shared symbolic-vs-expansionist pattern.

## Remaining risks

- Because helper bodies were not audited, helper-mediated idea churn or generic hidden effects may still exist outside the focus files.
- The route-lock finding is intentionally unpatched here because it changes playable route behavior beyond a tiny layout fix.
- Existing worktree state includes many unrelated modified and untracked files; this handoff only claims the two local coordinate edits listed above.
