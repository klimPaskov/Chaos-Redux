# Event 005 Parent Focus Release/Layout/Depth Tranche

Date: 2026-06-05 14:18 UTC

## Scope

Parent-agent patch tranche for Soviet Collapse release pacing and focus-tree cleanup. This is not a completion report for the full Event 005 rework.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `docs/events/005_soviet_collapse.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md`

## Release Pacing State

- Calm-world first-wave releases remain limited to base Soviet republic tags.
- Non-base and niche republics now remain behind the progressive follow-on candidate path.
- The follow-on path requires Gathering Storm or higher plus live crisis pressure such as Union Collapse Threat, progressive release pressure, failed-objective pressure, regional cascade pressure, war pressure, severe component pressure, or high urgency.
- Higher chaos raises follow-on burst size after those pressure gates are met. It does not make ordinary monthly progression release every possible country immediately.
- Union Unmade and triggerable scenario terminal paths remain the exhaustive rupture paths.

## Focus Layout Changes

- Fixed the audited Belarus upward/crossing pathline around:
  - `blr_soviet_collapse_the_green_border`
  - `blr_soviet_collapse_the_green_rail_pact`
  - `blr_soviet_collapse_partisans_or_army`
  - related forest-branch children
- Spread the Ukraine diplomacy/industry row conflict between:
  - `ukr_soviet_collapse_open_the_liaison_offices`
  - `ukr_soviet_collapse_black_sea_port_ledgers`
- Reworked the MFR route fork and worker-production payoff rows so the scoped parser finds no parent-on-same-row or upward prerequisite lines for the MFR tree.

## Focus Reward/Depth Changes

- `PRA_switchyard_denial_posts` now advances the rail authority mechanic instead of only placing bunkers:
  - opens mobile supply yard deployment
  - raises rolling stock and rail authority
  - improves depot control
  - builds supply/rail links in controlled core territory
  - expands the PRA corridor network
  - deploys rail guard columns
- `DSC_call_the_dead_soldiers_congress` now immediately behaves like a high-chaos dead-army opener:
  - hardens the existing dead-army idea path instead of adding another separate idea
  - opens field-hospital column deployment
  - grants a large assault manpower/equipment package
  - marks and cores controlled front-road claims
  - deploys assault columns
  - applies high-chaos neighbor expansion pressure

## Validation

- `git diff --check` passed for the edited focus/localisation files.
- Brace balance scan returned `0` for the edited Event 005 focus files.
- `rg "<=|>="` returned no unsupported operators in the edited Event 005 focus files.
- Mechanical focus audit across the four Event 005 focus files found:
  - `0` direct `add_ideas` focus rewards
  - `0` same-focus duplicate `add_ideas` rewards
- Scoped pathline parser found `0` parent-on-same-row/upward prerequisite issues for the patched Belarus/Ukraine/MFR areas.
- A fresh read-only focus audit subagent was spawned as `019e9820-60b3-7a80-a511-aa4ec20dd3b6` (`Copernicus`). It was still running when this handoff was written.

## Remaining Work

- The full user goal remains incomplete.
- The independent focus audit still needs to be collected and acted on.
- Many focus trees still require broader route-depth review and likely country-by-country rework for distinct political, industrial, military, diplomatic, and expansion branches.
- Chaos-country trees still need a larger pass so every special successor has an overpowered, lore-specific gameplay loop, not only stronger generic helpers.
- No flag sprite files were touched.

## Skills Used

- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
