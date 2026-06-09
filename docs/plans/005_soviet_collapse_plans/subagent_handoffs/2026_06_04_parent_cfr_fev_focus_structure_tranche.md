# Event 005 Parent Focus Structure Tranche

Date: 2026-06-04
Owner: parent Codex agent

## Scope

Bounded focus-tree cleanup for the current Soviet Collapse pass. This tranche targeted CFR layout/branch structure, one FEV Pacific interaction hook, and shared helper clutter. Flags and visual assets were intentionally not touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Main Changes

- CFR governance is no longer a four-way fake mutually-exclusive row. Those focuses now behave as separate political setup nodes instead of drawing exclusivity lines through the tree.
- CFR cabinet and plan-law joins were simplified so unrelated branches no longer all converge through one node.
- CFR branch lanes were separated into a compact structure:
  - left defense/construction battalion lane
  - central political/industry spine
  - right foreign-contract lane
  - far-right coercive/dark construction lane
- Removed the random anti-air building payoff from `soviet_collapse_apply_cfr_focus_worksite_gate_fortification`; it now builds infrastructure and site defenses.
- `FEV_pacific_observer_missions` now visibly unlocks `fev_negotiate_japanese_liaison_officers`.
- `soviet_collapse_apply_fev_pacific_japanese_liaison` now adds coastal port capacity, a dockyard, and naval experience in addition to fuel, convoys, recognition, intelligence, and Japan-facing opinion/AI pressure.
- Updated the FEV Pacific liaison tooltip to mention the unlocked talks and port expansion.

## Subagent Integration

Reviewed and accepted the bounded custom-splinter tooltip patch from `chaosx_focus_tree_auditor`:

- Handoff: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_191402_custom_splinter_reward_tooltip_patch.md`
- Patched focus IDs: `FTH_village_delegate_roads`, `KHC_laba_rear_area`, `FEV_war_plan`, `SZA_tomsk_omsk_switchyards`, `NLC_ration_and_signal_escorts`, `NLC_winter_road_columns`, `NLC_industry_plan`, `NLC_extreme_gate`

## Validation

- CFR static focus layout audit: 47 focuses, 0 mutual-exclusion declarations, 0 duplicate coordinates, 0 detected prerequisite-line crossings.
- Brace balance checked clean for touched focus/effect/localisation files.
- `git diff --check` clean for touched files.
- Unsupported operator scan found no `<=` or `>=` in touched files.
- UTF-8 BOM preserved for touched localisation and BOM-bearing focus file.
- `git status --short -- gfx/flags` showed no flag changes.

## Remaining Risks

- This does not complete the full Soviet Collapse focus-tree rework. Other republic and chaos trees still need the same branch-identity and line-overlap audit.
- CFR is cleaner and more purposeful, but this tranche did not redesign every reward in the factory successor file.
- FEV now has stronger Japan/Pacific interaction, but broader Far Eastern regional diplomacy and conflict paths still need a dedicated pass.
