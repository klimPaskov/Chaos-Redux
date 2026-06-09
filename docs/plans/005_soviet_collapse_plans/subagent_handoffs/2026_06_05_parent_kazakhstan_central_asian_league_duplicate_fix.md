# Parent Tranche: Kazakhstan Central Asian League Duplicate Fix

## Scope

Fixed the case where Kazakhstan could found a second Central Asian League after another Central Asian breakaway had already formed the regional faction.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Implementation

- Added `has_soviet_collapse_existing_central_asian_league_leader`.
  - It detects an existing Central Asian League founder that is still the faction leader.
  - It uses the same regional country set already used by the Central Asian league system: `UZB`, `KYR`, `TAJ`, `TMS`, `KAZ`, `BSC`, `TNC`, and `ALA`.
- Updated `can_found_soviet_collapse_central_asian_league` so a new league cannot be founded while an existing Central Asian League leader exists.
- Updated `can_found_soviet_collapse_central_asian_league` so a new league also cannot be founded after the Central Asian League announcement flag is set.
- Added `can_join_soviet_collapse_existing_central_asian_league`.
  - It keeps the same dynamic Central Asian candidate set as the league founder logic.
  - It lets an eligible, unfactioned Central Asian breakaway see the league decision when an existing Central Asian League leader is already present.
- Added `soviet_collapse_join_existing_central_asian_league`.
  - If a valid Central Asian league leader exists and `ROOT` is not already in a faction, the existing leader adds `ROOT` to its faction.
  - The joining country receives the existing Central Asian league member flags and regional faction common setup.
- Updated both normal and terminal Central Asian league founding helpers:
  - `soviet_collapse_found_central_asian_league`
  - `soviet_collapse_found_terminal_central_asian_league`
  - Both now join the existing league instead of creating a duplicate if the league already exists.
- Updated the normal decision path so joining an existing league spends the same displayed political power and command power cost as the formation decision.
- Updated the regional faction category and `soviet_collapse_found_steppe_federation` decision visibility so Kazakhstan and other eligible Central Asian breakaways can access the join path instead of only seeing the foundation path.
- Updated the decision name, description, and tooltip so the UI describes the join-or-found behavior and no longer says Kazakhstan must wait for three smaller republics when joining an existing league.
- Removed the extra three-smaller-republic gate from the invitation path for Kazakhstan, so an existing Central Asian League can invite Kazakhstan directly when it is a free breakaway and not already in a faction.

## Validation

- Brace balance passed for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `common/decisions/categories/005_soviet_collapse_categories.txt`
  - `localisation/english/005_soviet_collapse_l_english.yml`
- `git diff --check` passed for the touched Event005 script files.
- Localisation file still has a UTF-8 BOM.

## Remaining Risks

- This fixes duplicate Central Asian League creation, but does not redesign regional league membership UI or localisation text.
- The broader Event005 goal remains incomplete: focus-tree depth/layout, crisis shutdown behavior, and generic helper reward variety still need additional passes.
