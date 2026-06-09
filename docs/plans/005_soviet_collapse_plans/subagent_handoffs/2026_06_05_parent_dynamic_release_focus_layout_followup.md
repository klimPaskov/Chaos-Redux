# Event005 Parent Tranche: Dynamic Release Gate And Focus Layout Follow-Up

Date: 2026-06-05

## Scope

Parent implementation pass after the user clarified that non-base Soviet republic releases must depend on dynamic crisis pressure, not fire instantly on calm settings.

Touched files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Read-only verification covered:

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`

No flag or gfx assets were touched.

## Release Gate Check

The current release structure already matches the user's dynamic requirement:

- First-wave and first-year backlog releases use `is_soviet_collapse_first_wave_release_candidate`, which is limited to base republic tags.
- Non-base/internal republics use `has_soviet_collapse_dynamic_follow_on_release_pressure`, which requires a non-calm chaos tier plus live pressure such as Union Threat, release urgency, sustained progressive pressure, component pressure, failures, regional cascade, or war pressure.
- Pressure successors remain gated to chaos tier 3 or higher, terminal collapse, or severe live pressure.

No release-script change was made in this tranche because the existing post-tranche logic already keeps calm-world releases base-only while allowing Gathering Storm+ releases through live crisis pressure.

## Focus Layout Changes

Cleaned several audited long path joins without spreading whole trees out:

- Ukraine diplomacy branch: moved the foreign-court/liaison follow-up cluster closer to its actual branch and shortened follow-up lines.
- Ukraine high-chaos bread route: removed the distant `appointed_governors` prerequisite from `ukr_soviet_collapse_grain_census_of_everyone`; it now depends on the bread-state route nodes that actually feed it.
- Central Asia: changed `central_asia_soviet_collapse_the_southern_shield` from a huge all-route convergence into nearby structural prerequisites while keeping route completion checks in `available`.
- Moldova: moved `moldova_soviet_collapse_republic_of_crossings` into the central branch and stopped drawing long lines from every side branch; route checks remain in `available`.
- Belarus: moved `blr_soviet_collapse_league_supply_timetables` beside the timetable branch instead of drawing a line across the tree.
- Kazakhstan: moved the federation/arbitration chain closer to its southern-pact branch and replaced the long visible mutual-exclusion line between federation and lone-steppe routes with hidden completion locks.

## Focus Reward Changes

Strengthened the Construction Directorate's civilian-industry identity:

- `CFR_a_civilian_factory_in_every_capital` now unlocks the full construction decision ladder instead of only giving a repeated construction packet.
- `CFR_the_state_that_builds` now explicitly surges the city network and unlocks survey, contracts, idle-queue seizure, and factory-city belt decisions.
- `CFR_the_builder_state_marches_east`, `CFR_build_the_border_bend_the_border`, and `CFR_rebuild_russia_without_moscow` now connect expansion focuses back to reconstruction decisions and the factory-city belt.

## Validation

- `git diff --check` passed for both touched focus files.
- Brace balance is `0` for both touched focus files.
- No raw `<=` or `>=` operators were found in the touched focus files.
- Direct focus reward idea scan across all Event005 focus files returned:
  - `005_soviet_collapse_republics.txt`: `0` direct `add_ideas` focuses, `0` duplicate idea focuses
  - `005_soviet_collapse_custom_splinters.txt`: `0` direct `add_ideas` focuses, `0` duplicate idea focuses
  - `005_soviet_collapse_factory_successors.txt`: `0` direct `add_ideas` focuses, `0` duplicate idea focuses
  - `005_soviet_collapse_ancient_restorations.txt`: `0` direct `add_ideas` focuses, `0` duplicate idea focuses
- Focus coordinate/prerequisite scan confirmed the patched joins are now local, except Ukraine foreign courts still has a moderate `dx=10` from the statehood question because it remains a genuine diplomacy branch off the statehood fork.

## Remaining Gaps

- This is not a full focus-tree completion pass. Many trees still need further branch-depth cleanup, especially short high-chaos and ancient trees.
- The focus tree audit still lists other wide joins outside this tranche, including FEV/SZA/BAC/ARD endgame joins and several custom splinter template skeletons.
- A full final completion claim still requires a new full-tree audit after additional passes.
