# Event 005 Soviet Collapse Focus Cleanup Tranche

Date: 2026-06-04

## Scope

Parent-agent tranche for the Soviet Collapse focus-tree cleanup request. This is not a completion claim for the full event-wide focus rework.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Implemented

- Moved Ukraine's continuous focus panel to the far right of the tree so it no longer sits over the playable branch area.
- Removed the visible mutually-exclusive path lines between `ukr_soviet_collapse_army_supremacy` and `ukr_soviet_collapse_mixed_emergency_cabinet`.
  - The route choice still locks through hidden availability checks after either branch is completed.
- Removed the visible mutually-exclusive path lines between `ukr_soviet_collapse_the_double_republic` and `ukr_soviet_collapse_the_commune_war`.
- Shifted Ukraine's high-chaos bread-state lane to the far-right expansion/chaos area so it no longer cuts through normal political and military branches.
- Cleaned the shared breakaway focus tree opening into clearer lanes:
  - Political identity begins on the left with `soviet_collapse_the_republic_defines_itself`.
  - Ministry ledger/depot repair/home industry focuses now form the central industry lane.
  - Radio guard, field battalions, engineer rosters, and factory defense now form the right military/emergency lane.
  - `soviet_collapse_home_industry_contracts` now depends on depot repair instead of factory defense committees.
- Added a concrete Far Eastern Japan-facing mechanic:
  - `internal_soviet_collapse_far_eastern_port_authority` now unlocks `soviet_collapse_negotiate_pacific_liaison_officers`.
  - The new decision is visible only for breakaway countries with the Far Eastern port protocol flag and only if Japan exists.
  - The decision spends the existing breakaway recognition cost through `soviet_collapse_apply_breakaway_recognition_request`.
  - The new ROOT-scoped helper `soviet_collapse_apply_internal_far_eastern_japanese_contact` gives fuel, convoy access, recognition, liaison reach, decryption against Japan, Japan support AI strategy, and raises Moscow foreign/depot pressure.
  - `internal_soviet_collapse_pacific_harbor_guard` reinforces the same Japan-facing channel if Japan exists.

## Validation

- `git diff --check` passed for touched script/localisation files.
- Brace balance is zero for:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
- No `<=` or `>=` found in touched script files.
- Ukraine focus duplicate-coordinate scan reports `0` duplicate coordinates.
- New localisation keys each appear exactly once.
- `gfx/flags` was not touched.

## Remaining Risk

- The full event-wide focus cleanup is still incomplete. Other republics and custom successors still contain visible mutually-exclusive path lines, dense layouts, and generic helper reward patterns that need separate passes.
- Some older unrelated edits are present in the same files; they were not reverted or included in this tranche intentionally.
