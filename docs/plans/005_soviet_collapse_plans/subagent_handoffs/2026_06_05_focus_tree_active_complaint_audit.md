# Event005 Focus Tree Active Complaint Audit

Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, `localisation/english/005_soviet_collapse*.yml`, and `docs/events/005_soviet_collapse.md`.

This was a read-only audit. No gameplay, localisation, gfx, flag, or sprite files were changed.

## Ranked Findings

1. **Broad tree-structure gap remains in the short high-chaos and ancient trees.** The 16-18 focus trees are still too compact to satisfy major-country branch standards. `TSC_soviet_collapse_focus_tree` has 18 focuses starting at `005_soviet_collapse_custom_splinters.txt:1837`, `RMC_soviet_collapse_focus_tree` has 18 at `005_soviet_collapse_custom_splinters.txt:2348`, and each ancient restoration tree has 16, beginning with `KZR_soviet_collapse_ancient_focus_tree` at `005_soviet_collapse_ancient_restorations.txt:13`. Their visible structure is usually one opening stem, one small industry/support side, one symbolic/settlement route, and one expansion route, not distinct political, industrial, expansion, military, diplomatic, and late-game families.

2. **Direct idea-spam is mostly fixed, but repeated helper payloads still read like reward spam.** The four scoped focus files currently have no direct `add_ideas =` in focus rewards. The likely repeated-spirit helpers have been replaced by consolidated variable/flag helpers: `soviet_collapse_update_consolidated_republic_ideas` clears old staged ideas at `005_soviet_collapse_effects.txt:6046`, and `soviet_collapse_clear_focus_starting_tension_ideas` removes old starting-tension spirits at `005_soviet_collapse_effects.txt:6061`. The remaining repeated pattern is many focuses calling broad helpers such as `soviet_collapse_apply_focus_high_chaos_identity` from `TSC_recover_the_burned_glass` at `005_soviet_collapse_custom_splinters.txt:1940`, `RMC_open_the_red_martyrology` at `005_soviet_collapse_custom_splinters.txt:2366`, and `ukr_soviet_collapse_the_bread_line_becomes_a_border` at `005_soviet_collapse_republics.txt:2028`. That helper is flag-gated for the heavy payload (`005_soviet_collapse_effects.txt:9066` and `005_soviet_collapse_effects.txt:11409`), so it is not a clean duplicate-idea bug; it is a route-payoff repetition problem.

3. **Stockpile rewards are still too frequent in custom splinter trees.** `005_soviet_collapse_custom_splinters.txt` has 132 direct `add_equipment_to_stockpile` call lines. Worst visible clusters include `ARD` convoy rewards at `005_soviet_collapse_custom_splinters.txt:23729`, `23785`, `24093`, `24115`, `24188`, and `24216`; `KHC` support/artillery rewards at `15375`, `15507`, `15534`, `15660`, `15680`, `15705`, `15754`, `15778`, `15804`, and `15972`; and `GAC` support-equipment repetition at `13130`, `13174`, `13296`, `13320`, `13348`, and `13451`. These should be converted into route-specific decisions, unit unlocks, timed missions, claims/cores, leader/advisor changes, or named logistics mechanics.

4. **Ancient restoration branches are real but too shallow.** The KZR example shows the pattern: politics opens at `KZR_restore_itil_council` (`005_soviet_collapse_ancient_restorations.txt:29`), industry is mostly `KZR_ferry_house_registers` and two children (`56`, `70`, `84`), military is `KZR_volga_toll_guard` plus children (`98`, `115`, `129`), and expansion is mainly `KZR_old_border_files` into `KZR_expansionist_steppe_levy` (`176`, `239`). The final route choice is only one symbolic focus versus one expansion focus (`213`, `240`) before `KZR_khazar_charter` (`287`). SOG/KHW/ALN repeat this compact shape.

5. **Some high-chaos trees are aggressive enough at endpoints but not along the route.** Strong endpoint examples exist: `PRA_rails_over_capitals` creates a Soviet war goal and AI hostility at `005_soviet_collapse_custom_splinters.txt:1739`, `TSC_starfall_mandate` does the same at `2266`, `DSC_congress_of_the_dead_army` escalates to war at `3268`, and `KZR_expansionist_steppe_levy` does it at `005_soviet_collapse_ancient_restorations.txt:240`. The problem is that many earlier focuses on those paths still give stockpiles, single-state construction, or variable ticks before the endpoint instead of continuously opening attacks, raids, mandate decisions, or aggressive neighbor pressure.

6. **Visible pathline and route-lock issues are broad, not safe single-line fixes.** `TSC_observatory_state` has a visible prerequisite from `TSC_league_of_clear_signals` but a hidden `available` gate on `TSC_portable_laboratory_trains` (`005_soviet_collapse_custom_splinters.txt:2305`, `2311`, `2312`), so the displayed route does not show the real requirement. `RMC_republic_of_witnesses` similarly displays a League prerequisite but secretly requires `RMC_shrine_foundries` (`2736`, `2742`, `2743`). `PRA_rails_over_capitals` and `PRA_the_pale_line_endures` are mutually exclusive across different branches and rows (`1739`, `1746`, `1808`, `1815`), which likely creates an awkward cross-tree exclusion arrow. These should be handled as layout redesigns, not isolated coordinate nudges.

7. **The large republic trees are improved but still uneven.** Ukraine and Kazakhstan have many focuses (`ukr` tree starts at `005_soviet_collapse_republics.txt:18`, 83 focuses; `kaz` starts at `10163`, 92 focuses), with real branch families. The remaining issues are route sprawl and hidden gates: for example, Ukraine mixes League, diplomacy, army, bread-state, and expansion paths across very wide x positions from `ukr_soviet_collapse_prepare_league_liaison_rooms` at `1427` through `ukr_soviet_collapse_last_harvest_plan` at `2197`, making branch identity hard to scan even when individual rewards are meaningful.

## Recommended Parent Patches

1. Rework the 16-18 focus high-chaos and ancient trees first. Add visible political, industry, military, expansion, and diplomacy lanes with 3-5 focuses each, plus at least one decision unlock or route mechanic per lane.

2. Convert clustered stockpile rewards in ARD, KHC, GAC, KRS, UWD, BAC, NLC, BSC, DHC, and FEV into route mechanics: staged raids, port/rail/convoy missions, claim-and-core packages, named unit templates, or decision tiers.

3. Do a layout-only pass after the structural redesign. Avoid hidden `available = { has_completed_focus = ... }` gates where a visible prerequisite would explain the path, unless adding the visible line creates worse crossings.

4. Keep the consolidated idea model. Do not return to direct focus `add_ideas`; the remaining problem is payoff variety and route depth, not literal duplicate focus spirits.

## Validation

- Read required repo skills: `chaos-redux-subagents`, `hoi4-focus-trees`, and `hoi4-decisions-missions`.
- Consulted offline wiki pages: data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and national focus modding.
- Consulted vanilla documentation under `~/projects/Hearts of Iron IV/documentation` and inspected vanilla focus/decision precedents.
- Ran read-only searches/parsing for focus counts, direct `add_ideas`, direct stockpile rewards, helper call sites, and route/layout anomalies.

## Skills Used

- `chaos-redux-subagents`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
