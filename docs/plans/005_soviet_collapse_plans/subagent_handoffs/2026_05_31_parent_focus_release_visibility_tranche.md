# Event005 Parent Focus/Release/Visibility Tranche

Date: 2026-05-31

## Scope

Parent-owned tranche after the factory/ancient focus audit subagent completed.

Files changed by this tranche:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

No flag files were read, edited, converted, or touched.

## Focus Reward Cleanup

The remaining obvious helper-stack focus rewards were audited across:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Before this tranche, the local audit found one Ukraine focus and five custom-splinter focuses with three or more broad reward helpers inside one `completion_reward`.

Patched focus ids:

- `ukr_soviet_collapse_black_sea_hegemony`
- `FTH_communes_without_capitals`
- `PRA_rails_over_capitals`
- `DHC_steppe_watch_posts`
- `KHC_steppe_watch_posts`
- `SZA_station_fortress_line`

Behavior after patch:

- Ukraine's Black Sea branch now calls one composite package, `ukr_soviet_collapse_apply_black_sea_hegemony_package`, under a single player-facing tooltip.
- FTH, PRA, DHC, KHC, and SZA now use a single high-chaos identity package with direct state construction or route payoff rather than stacking rail/mobile/claim/neighbor-conflict helpers in the focus block.
- A follow-up audit over all four Event005 focus files found no focus `completion_reward` with three or more broad `soviet_collapse_apply_*` or route helper calls, and no direct `add_ideas` / `add_timed_idea` entries in those focus rewards.

## Release and Scenario Evidence

Current implementation evidence inspected:

- `soviet_collapse_release_dynamic_follow_on_republics` scales follow-on and internal releases by chaos tier, with `soviet_collapse_evolution_first_wave_recorded` using the gathering-storm release constants.
- `is_soviet_collapse_dynamic_union_progressive_release_candidate` allows any possible non-SOV country with cores in original union, SOV, subject, breakaway, event-created, or high-chaos-controlled Soviet-collapse territory after first-wave/gathering-storm state or chaos tier flags.
- Explicit progressive release weights include niche/internal tags such as `YAM`, `TAY`, `NEN`, `DON`, `KUB`, `BUK`, `ALT`, `KAL`, `CIN`, `DAG`, `CKK`, `VLA`, `KKP`, `OVO`, `ABK`, `KBK`, `NOA`, `VGE`, `KHI`, `UDM`, `CHU`, and `MEL`.
- `soviet_collapse_apply_terminal_collapse` runs ordinary releases, exhaustive `every_possible_country` release passes, SOV subject freeing, another exhaustive pass, terminal league formation, anti-SOV war joining, and breakaway-on-breakaway wars.
- `soviet_collapse_force_triggerable_scenario_terminal_release` uses the same exhaustive release passes, frees SOV subjects, applies dynamic initial forces, and includes all chaos successors when `soviet_collapse_triggerable_scenario_include_chaos` is set.
- `suppress_soviet_collapse_fire_once_for_triggerable_scenario` is called at triggerable scenario launch and removes Event005 from the fire-once array, records it as fired/disabled, sets its weight to zero, and marks the scenario suppression flag.

## Decision Visibility Evidence

Current implementation evidence inspected:

- The compact foreign patron category has a `soviet_collapse_open_republic_aid_menu` decision and matching `soviet_collapse_close_republic_aid_menu` decision.
- Selected targets are stored with `soviet_collapse_foreign_patron_selected_target`, the selected country id variable, the selected influence variable, and `soviet_collapse_foreign_patron_menu_open`.
- Opening the target refreshes the breakaway registry, ensures the target is in `global.soviet_collapse_breakaway_countries`, activates targeted decisions for the selected target/event target, and forces breakaway component variables to exist.
- Targeted intervention decisions have selected-target bypass branches, so the chosen breakaway should remain visible even if ordinary aid route checks would otherwise hide non-selected targets.

Remaining risk: `activate_targeted_decision` still uses dynamic scope targets (`FROM`, `PREV`, and `event_target:`). The target-array path should cover selected targets, but if the engine rejects dynamic activation targets at runtime, the next patch should replace those activation calls with a static-target or meta-effect activation helper.

## Validation

Commands run:

- Brace-depth validation for Event005 focus files, scripted effects, scripted triggers, decisions, triggerable scenario effects, and events: all `depth=0`, no negative depth.
- `git diff --check` on the touched Event005 files: passed.
- `rg -n "<=|>="` on the touched Event005 files: no matches.
- `git diff --name-only -- gfx/flags`: empty.

## Remaining Gaps

- This tranche reduces the worst remaining focus reward spam but does not complete the requested full focus-tree rework. OGB, several compact ancient trees, and some chaos successors still need deeper route families.
- Layout/pathline quality still needs a rendered or coordinate-based audit pass; this tranche only touched reward helper stacks.
- Evolution detail spreadsheet parity still needs a dedicated localisation/spreadsheet pass.
- The foreign patron selected-target decisions appear structurally correct, but runtime confirmation is still pending for the reported Tajikistan case.
