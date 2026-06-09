# Event005 Parent Focus Reward/Layout Tranche 2

## Scope

This parent tranche followed the fresh focus audit and only touched a bounded set of Event005 focus issues. Flag assets were explicitly left untouched.

## Changes

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - Cleaned `DSC_claim_the_soldiers_road` visible reward spam by replacing several visible helper calls with one purpose-written tooltip and hidden payload calls.
  - Preserved the existing gameplay payloads: front-road claims, controlled-state cores, expansion claims, assault columns, and dead-army neighbor war orders.

- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
  - Added `dsc_claim_the_soldiers_road_focus_tt` to describe the combined Dead Soldiers Congress road reward in one player-facing tooltip.

- `common/national_focus/005_soviet_collapse_republics.txt`
  - Moved `moldova_soviet_collapse_western_training_mission` from `x = 20` to `x = 22`.
  - This removes the visible pathline running through `moldova_soviet_collapse_southern_rail_timetables` while keeping the Moldova branch compact.

## Audited But Not Changed

- `central_asia_soviet_collapse_khwarazm_restoration_debate`
  - The apparent duplicate `add_state_claim` entries are split across mutually exclusive tag branches. Only one branch fires for a country, so this is not a same-runtime duplicate reward.

- `OGB_claim_the_old_trade_cities`
  - The apparent repeated `is_controlled_by = ROOT` and `add_core_of = ROOT` blocks are scoped to different state IDs. They are intentional per-state checks, not duplicated effects on one state.

## Remaining Risks

- This does not complete the full focus-tree cleanup goal. The larger remaining work is still the deep design pass: more meaningful focus-to-mechanic integration, route identity, Ukraine/Belarus tree readability, and reducing repeated helper/tooltips across all republic and chaos trees.
- The worktree contains many earlier Event005 and unrelated Event006 changes. This handoff only describes the scoped changes above.
