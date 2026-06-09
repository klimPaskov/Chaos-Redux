# Event 005 Focus Branch Cleanup Tranche

## Scope

Parent implementation tranche for the ongoing Soviet Collapse focus-tree cleanup.

## Changes

- Moved Ukraine's continuous-focus panel away from the opening focus-tree rows so it no longer sits over the active tree view.
- Moved `ukr_soviet_collapse_rural_deputy_bloc` out from between the `army_supremacy` / `mixed_emergency_cabinet` mutually exclusive pair.
- Reduced repeated Japan liaison payloads in the Far Eastern Republic Pacific branch:
  - `FEV_pacific_observer_missions` now establishes the liaison and unlock surface.
  - `FEV_sakhalin_ferry_protocols` now gives concrete ferry/port/fuel logistics instead of reapplying the same liaison helper.
  - `FEV_pacific_city_compact` now consolidates recognition and coastal industry instead of repeating the liaison helper.
- Added `fev_negotiate_japanese_liaison_officers`, a Japan-gated decision unlocked by `FEV_pacific_observer_missions`.

## Validation

- `git diff --check` passed on touched Soviet Collapse script files.
- Brace balance passed for touched focus and decision files.
- Unsupported `<=` / `>=` operators were not found in touched focus and decision files.
- `gfx/flags` has no working-tree changes.

## Remaining Risks

- This is not a full focus-tree rewrite. The broad issue remains: several Soviet Collapse trees still need branch-level simplification, reward-depth cleanup, and visual pathline review.
- The FEV decision uses an existing decision icon until a dedicated Japan liaison icon is registered or provided.
