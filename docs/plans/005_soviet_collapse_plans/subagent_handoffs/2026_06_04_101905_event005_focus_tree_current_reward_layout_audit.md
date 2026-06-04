# Event005 Focus Tree Current Reward/Layout Audit

Date: 2026-06-04 10:19 UTC

Role: Chaos Redux focus-tree auditor subagent.

## Scope

Audited the current worktree after the parent removed the generic high-chaos escalation wrapper from ordinary focus helpers and patched Ukraine/Belarus pathlines. I kept gameplay files read-only. No focus-file, scripted-effect, gfx, interface, `.tga`, or flag asset patch was made.

## Required references used

- Repo skill: `hoi4-focus-trees`.
- Offline wiki pages opened: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs consulted: `effects_documentation.md` for `load_focus_tree` / `mark_focus_tree_layout_dirty`, `triggers_documentation.md` for `has_focus_tree`.
- Vanilla focus precedents skimmed: `common/national_focus/soviet.txt`, `generic.txt`, `poland.txt`.

## Files inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` read-only, to understand helper side effects only.

## Files changed

- Added this handoff only: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_101905_event005_focus_tree_current_reward_layout_audit.md`

## Idea spam audit

No direct focus reward `add_ideas`, `add_timed_idea`, `remove_ideas`, or `swap_ideas` operations remain in the four audited focus files.

The largest remaining visible-spirit churn risk is indirect: ordinary helper call sites still funnel through `soviet_collapse_add_republic_focus_recovery_progress`, which calls `soviet_collapse_update_consolidated_republic_ideas` once per focus effect chain. That updater is now mostly clamp/cleanup logic, so the parent cleanup succeeded in removing direct staged-idea spam from focus files. It can still visibly remove/resolve startup disorder ideas at recovery thresholds, but I did not find focus-local idea spam to patch safely.

High-volume helper call sites remain mechanically repetitive:

- `soviet_collapse_apply_focus_depot_and_supply_control`: 141 focus calls.
- `soviet_collapse_apply_focus_military_consolidation`: 132 focus calls.
- `soviet_collapse_apply_focus_legal_recognition`: 108 focus calls.
- `soviet_collapse_apply_focus_republican_compact_plan`: 80 focus calls.
- `soviet_collapse_apply_focus_foreign_channel`: 65 focus calls.
- `soviet_collapse_apply_focus_high_chaos_identity`: 60 focus calls.

## Worst Remaining Shallow Reward Examples

- `OGB_future_bulgaria_file` at `005_soviet_collapse_factory_successors.txt:1579`: decision tooltip, political power, and `ogb_volga_legitimacy` only. It sets up future Bulgaria flavor, but the focus itself has no immediate claim/integration/settlement action.
- `MFR_war_market_never_sleeps` at `005_soviet_collapse_factory_successors.txt:2804`: pure helper call site. Needs a visible market/contract unlock, arms export decision, sponsor dependency consequence, or client-armament payoff.
- `MFR_output_is_victory` at `005_soviet_collapse_factory_successors.txt:2878`: pure helper call site behind the eternal arsenal route. The route name promises a major doctrine/production state but the focus-level reward is opaque.
- `MFR_no_peace_without_orders` at `005_soviet_collapse_factory_successors.txt:2916`: helper plus war support. It is late route content and should create a clear war-market/faction/contract consequence.
- `ukr_soviet_collapse_the_bread_line_becomes_a_border`, `ukr_soviet_collapse_black_soil_oath`, `ukr_soviet_collapse_grain_census_of_everyone`, `ukr_soviet_collapse_no_one_leaves_the_bread_line`, and `ukr_soviet_collapse_when_the_fields_refuse_the_state`: high-chaos branch focuses mostly call high-chaos/chaos helpers plus small stat changes. Because `soviet_collapse_apply_high_chaos_focus_payload` is guarded as a once-per-country payload, later calls can feel like shallow repeaters.
- `kaz_soviet_collapse_alash_memory_restored` and `kaz_soviet_collapse_socialist_steppe_republic`: route identity locks currently resolve through one standard helper each; they need immediate distinct visible route unlocks or country-identity consequences.

## Pathline And Mutex Risks

Validation found no duplicate focus ids, no missing prerequisites, no prerequisites placed on the same row, no child placed above its prerequisite, and no asymmetric mutual exclusions.

Remaining pathline risk is long one-row lateral edges. Exact worst examples:

- `ukr_soviet_collapse_british_caution` at `005_soviet_collapse_republics.txt:1379`: x31/y5 from `ukr_soviet_collapse_foreign_courts_notice_kyiv` x20/y4.
- `ukr_soviet_collapse_romanian_grain_and_river_bargain` at `005_soviet_collapse_republics.txt:1614`: x34/y7 from `ukr_soviet_collapse_romanian_port_route` x24/y6.
- `blr_soviet_collapse_minsk_supplies_the_front` at `005_soviet_collapse_republics.txt:9721`: x18/y11 from `blr_soviet_collapse_baltic_wire_rooms` x27/y10. This is improved from the broad Belarus issue but still a long diagonal edge.
- `kaz_soviet_collapse_the_congress_chooses_a_past` at `005_soviet_collapse_republics.txt:10083`: x23/y2 from x9/y1 and x13/y1 parents; the route fork still pulls across the trunk.
- `kaz_soviet_collapse_alash_memory_restored` at `005_soviet_collapse_republics.txt:10170`: x36/y3 from `kaz_soviet_collapse_the_congress_chooses_a_past` x23/y2.
- `kaz_soviet_collapse_the_alash_courts` at `005_soviet_collapse_republics.txt:10241`: x22/y4 from `kaz_soviet_collapse_alash_memory_restored` x36/y3.
- `DHC_river_and_steppe_compact` at `005_soviet_collapse_custom_splinters.txt:14669`: x12/y10 from `DHC_hardline_against_commissars` x2/y9.
- `UWD_workers_canteen_compact` at `005_soviet_collapse_custom_splinters.txt:19120` and `UWD_kama_foundry_contracts` at `19154`: compact crosses from x6/y6 to x16/y7, then back to x3/y8.
- `BAC_militia_training_yards` at `005_soviet_collapse_custom_splinters.txt:22551`: x15/y9 from `BAC_war_plan` x0/y8.

## Concrete Next Targets

1. Rework the Kazakhstan early fork geometry around `kaz_soviet_collapse_the_congress_chooses_a_past`, `kaz_soviet_collapse_alash_memory_restored`, `kaz_soviet_collapse_socialist_steppe_republic`, `kaz_soviet_collapse_resource_defense_directorate`, and `kaz_soviet_collapse_the_alash_courts`. This is the worst current pathline cluster.
2. Add visible late-route payoff to MFR focuses `MFR_war_market_never_sleeps`, `MFR_output_is_victory`, and `MFR_no_peace_without_orders`: decisions, arms-client mechanics, contract missions, or sponsor/dependency consequences.
3. Add a concrete OGB payoff to `OGB_future_bulgaria_file`: claim preparation, trade-city integration, court/archive decision unlock, or future-Bulgaria event hook with visible player action.
4. Thin repeated high-chaos helper-only call sites in Ukraine by giving later bread-state focuses unique branch consequences instead of relying on the once-per-country high-chaos payload.
5. Repair the DHC/UWD/BAC custom-splinter long lateral lines in a focused layout-only pass after the Kazakhstan tranche.

## Validation

- Brace balance over all four audited focus files: clean, final balance 0, no early closes.
- `rg "<=|>="` over all four audited focus files: no unsupported operators found.
- Direct focus-file idea operations audit: no `add_ideas`, `add_timed_idea`, `remove_ideas`, or `swap_ideas` found.
- Duplicate focus id audit over audited files: 0 duplicates.
- Missing prerequisite audit: 0 missing prerequisites.
- Mutual exclusion symmetry audit: 0 asymmetric mutex links.
- Flag asset status: untouched. I did not edit `gfx/flags`, `interface/flags`, any `.tga`, or any flag asset path.

## Simplifications, omissions, and blockers

No gameplay simplification was made because no gameplay patch was made. The audit is incomplete as a completion claim for Event005 focus-tree quality: the remaining reward-depth and layout issues above need implementation tranches before the focus-tree concern can be considered resolved.
