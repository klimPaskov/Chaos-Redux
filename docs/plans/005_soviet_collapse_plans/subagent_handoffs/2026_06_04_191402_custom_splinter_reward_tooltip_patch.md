# Event 005 Custom Splinter Reward Tooltip Patch Handoff

Subagent: `chaosx_focus_tree_auditor`
Date: 2026-06-04 19:14 UTC
Scope: bounded patch to `common/national_focus/005_soviet_collapse_custom_splinters.txt` only, plus this handoff. No commits made.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_191402_custom_splinter_reward_tooltip_patch.md`

## Focus IDs Changed

- `FTH_village_delegate_roads`
- `KHC_laba_rear_area`
- `FEV_war_plan`
- `SZA_tomsk_omsk_switchyards`
- `NLC_ration_and_signal_escorts`
- `NLC_winter_road_columns`
- `NLC_industry_plan`
- `NLC_extreme_gate`

## Behavior Before And After

Before:

- These focuses exposed repeated flat reward lines directly in the focus completion tooltip: random infrastructure/rail/radar/bunker/factory construction, support equipment, XP, decryption, variable bumps, and repeated recovery/helper calls.
- Several focuses already had useful custom tooltips, but the underlying flat effects still displayed below the tooltip.

After:

- The same gameplay effects remain in the same focus completion rewards.
- Repeated flat reward payloads now sit inside `hidden_effect = { ... }`.
- Each patched focus exposes one existing route-appropriate custom tooltip:
  - `FTH_supply_tt`
  - `soviet_collapse_custom_splinter_logistics_route_reward_tt`
  - `soviet_collapse_custom_splinter_expansion_route_reward_tt`
  - `soviet_collapse_custom_splinter_industrial_route_reward_tt`
  - `NLC_supply_tt`
  - `NLC_industry_plan_tt`
  - `NLC_extreme_gate_tt`

## Why This Is Bounded

- No new mechanics, helpers, decisions, flags, ideas, localisation keys, or assets were added.
- Existing effect order was preserved inside each reward as closely as possible.
- Existing tooltip localisation was reused, avoiding a localisation/BOM edit.
- `FEV_harbor_fortress_line` was inspected and left unchanged because its clutter payload was already behind `FEV_harbor_fortress_line_tt` and `hidden_effect`.

## Remaining Risks And Follow-Up

- This is only a tooltip-clutter patch. It does not solve the broader design issue that many custom splinter branches still rely on repeated helper payloads rather than distinct route mechanics.
- `NLC_apatity_rear_area`, `NLC_hidden_doctrine`, `SZA_winter_column_registers`, `FEV_winter_rail_columns`, and nearby construction/equipment focuses still have visible flat reward lines and should be handled in a later tranche if the parent wants the same cleanup applied more widely.
- The file had pre-existing uncommitted edits before this patch. This handoff only claims the focus IDs listed above.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_191402_custom_splinter_reward_tooltip_patch.md` returned clean for tracked diffs.
- `git diff --check --no-index -- /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_191402_custom_splinter_reward_tooltip_patch.md` returned clean for the new untracked handoff file.
- Brace balance check for `common/national_focus/005_soviet_collapse_custom_splinters.txt` returned `balance=0` and `min=0`.
- Note: the handoff file is newly untracked, so the normal tracked `git diff --check` does not include it until it is staged.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`
