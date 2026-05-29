# Factory Successor Focus Reward and AI Cleanup Handoff

Date: 2026-05-29

Scope:

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- No localisation edits.
- No triggerable scenario release logic, mission popups, flag assets, broad scripted release systems, prerequisites, mutual exclusions, or layout changes were intentionally edited by this pass.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | Added non-idea industrial, war-goal, AI-strategy, and filter cleanup rewards to CFR/MFR endgame focuses. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_factory_successor_reward_ai_cleanup_handoff.md` | This handoff. |

## Focus IDs Changed

| Focus id | Behavior before | Behavior after |
| --- | --- | --- |
| `CFR_a_civilian_factory_in_every_capital` | Called the existing foreign factory helper and League support variables, but only one helper-level factory payoff. | Also adds offsite civilian industry using `constant:soviet_collapse_factory_ancient.medium_mandate_gain`, making the construction-state branch visibly stronger without adding ideas. |
| `CFR_the_builder_state_marches_east` | Set route flag, public works helper, and small war support. | Also adds hidden AI pressure to conquer/antagonize `SOV` and continue civilian construction. |
| `CFR_rebuild_russia_without_moscow` | Rebuild helper only; no direct conquest payoff despite annexation-scale title. | Adds `FOCUS_FILTER_ANNEXATION`, offsite civilian industry, an annex-everything war goal against `SOV` when valid, and hidden AI conquer/antagonize/building strategies. |
| `MFR_every_order_a_rifle` | Existing arsenal/client arms helper only. | Also adds hidden AI pressure to conquer/antagonize `SOV` and prioritize arms factories. |
| `MFR_eternal_arsenal_marches` | Existing eternal arsenal helper only; no direct conquest payoff despite march/endgame title. | Adds `FOCUS_FILTER_ANNEXATION`, offsite military industry, an annex-everything war goal against `SOV` when valid, and hidden AI conquer/antagonize/arms-factory/template strategies. |

## Route Coverage Table

| Required route/content area | Implemented branch | Status | Notes |
| --- | --- | --- | --- |
| Construction/Factory directorate overpowered industry | `CFR_a_civilian_factory_in_every_capital`, `CFR_rebuild_russia_without_moscow` | Improved | Added direct offsite civilian industry to the mid/late CFR industrial payoff. |
| Construction directorate expansion pressure | `CFR_the_builder_state_marches_east`, `CFR_rebuild_russia_without_moscow` | Improved but not complete | Added SOV-directed AI aggression and a valid-gated SOV war goal at the endgame. No new release/formable systems added. |
| Military Factory of Russia arsenal threat | `MFR_every_order_a_rifle`, `MFR_eternal_arsenal_marches` | Improved | Added arms-factory AI targets and offsite military industry to the endgame. |
| MFR expansion pressure | `MFR_eternal_arsenal_marches` | Improved but not complete | Added SOV-directed AI aggression and a valid-gated SOV war goal. Broader neighbor/postwar systems remain parent-owned. |
| Idea-spam cleanup | CFR/MFR patched focuses | Clean | No `add_ideas`, `add_timed_idea`, or `swap_ideas` were added. |

## Coordinate/Layout Reconciliation

Per the parent scope update, I stopped layout work and did not intentionally edit `x`, `y`, `prerequisite`, or `mutually_exclusive` lines in this pass.

The current dirty diff for `005_soviet_collapse_factory_successors.txt` already contains coordinate-only changes that the parent should reconcile with the compact layout pass:

- `CFR_the_concrete_committee`
- `OGB_treat_with_idel_ural`
- `OGB_the_old_name_survives_modern_war`
- `MFR_armorers_elect_delegates`
- `MFR_rifles_before_speeches`
- `MFR_repair_the_tank_lines`
- `MFR_aircraft_parts_in_secret_workshops`
- `MFR_standardize_the_rifle_line`
- `MFR_shells_without_sleep`
- `MFR_battery_cities`
- `MFR_no_serial_numbers`
- `MFR_arsenal_protectorate_offer`
- `MFR_no_shell_without_obedience`
- `MFR_factory_guard_columns`
- `MFR_workers_must_not_flee`
- `MFR_builders_waste_steel`
- `MFR_civilian_factory_rivalry`
- `MFR_contracts_with_builders`
- `MFR_war_market_never_sleeps`

## Icon Coverage Table

| Surface | Status | Notes |
| --- | --- | --- |
| Patched focus icon ids | Unchanged | No new icon IDs or sprite references added. |
| Reward/filter match | Improved | Annexation filter added to the two focuses that now grant direct war goals. |
| Missing icons | Not checked mod-wide in this continuation | Earlier handoffs reported no missing focus icon assignments/sprite definitions for the broader focus files. |

## Localisation and Reward Mismatch List

| Area | Status | Notes |
| --- | --- | --- |
| Localisation keys | Unchanged | No player-facing strings changed. |
| `CFR_rebuild_russia_without_moscow` | Improved | Reward now matches the endgame title better through offsite industry, SOV war goal, and aggressive AI. |
| `MFR_eternal_arsenal_marches` | Improved | Reward now matches the title through offsite arms factories, SOV war goal, infantry template priority, and aggressive AI. |
| Idea spam | Clean in patched focuses | No new idea grants. |

## AI Behavior Gaps

- Improved: CFR and MFR endgame focuses now add direct AI strategy pressure instead of relying only on local `ai_will_do`.
- Remaining: OGB still has no comparable route-level AI conquest package in this pass.
- Remaining: MFR/CFR only target `SOV` directly here. Neighbor expansion, postwar coring, and protectorate/integration behavior remain parent-owned.
- Remaining: Current AI strategy values are focus-granted and persistent; no cleanup/removal hooks were added because that would touch broader systems.

## High-Priority Fixes

Completed:

1. Strengthened CFR industry without adding another idea.
2. Added CFR endgame SOV war goal and AI aggression.
3. Added MFR endgame SOV war goal and AI aggression.
4. Added annexation search filters where rewards now include direct war goals.

Remaining:

1. Parent should reconcile the current coordinate diffs with the compact layout pass.
2. Parent should decide whether to add broader target selection, coring, and postwar integration through existing decision/formable systems.
3. OGB and the shallow crisis splinters still need deeper dangerous behavior outside this narrow reward patch.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt localisation/english/005_soviet_collapse_l_english.yml`: passed.
- Focus reward scan on `005_soviet_collapse_factory_successors.txt`: 128 focuses, `direct add_ideas = 0`, `create_wargoal = 2`, `add_ai_strategy = 13`.
- Direct duplicate reward scan for `add_ideas`, stockpile rewards, offsite buildings, war goals, and AI strategies in individual factory-successor focus blocks: no duplicate lines reported.
- Quick layout/topology parser was run for awareness only after the parent scope update. I did not act on layout findings.

## Skipped Validation

- No in-game HOI4 load test was run.
- No full mod-wide validator was run because the worktree contains parent/user changes outside this subagent scope.
- No localisation encoding check was needed because localisation was not edited.

## Remaining Route Risks

- This is not a full Soviet Collapse focus-tree completion pass.
- The patch improves factory-successor payoff quality but does not solve all shallow/random reward patterns across republics and custom splinters.
- The direct SOV war goals are intentionally narrow and valid-gated. They do not replace parent-owned release logic, mission popups, or broad scripted release systems.
