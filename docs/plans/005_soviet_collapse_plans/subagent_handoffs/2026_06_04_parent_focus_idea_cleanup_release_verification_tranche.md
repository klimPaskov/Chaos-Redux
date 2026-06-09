# Event005 Parent Focus Idea Cleanup And Release Verification Tranche

## Scope

Continued the Soviet Collapse focus-tree cleanup goal without touching flag assets.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

## Gameplay Changes

- Added `soviet_collapse_clear_focus_starting_tension_ideas`.
- Replaced the remaining focus-local hidden `remove_ideas` calls for starting rivalry/disputed-name spirits with that shared helper.
- Preserved the existing player-facing resolution tooltips on the affected focuses.
- Reviewed the bounded focus audit subagent handoff and integrated high-confidence search-filter fixes for focuses with direct naval, airbase, anti-air, dockyard, or convoy rewards.

Affected focuses:

- `PRA_the_board_overrules_ministers`
- `TSC_the_committee_of_instruments`
- `RMC_communes_of_witnesses`
- `DSC_witness_officers`
- `NRF_living_harbor_committees`
- `ICD_commissars_of_last_addresses`
- `OGB_the_council_takes_the_seal`

Search-filter fixes added or integrated:

- `CFR_cities_first`: prerequisite fixed by focus audit subagent to sit under the same fork parent as the other CFR strategy choices.
- `ukr_soviet_collapse_direct_national_claims`: `FOCUS_FILTER_ANNEXATION` added by focus audit subagent.
- `NLC_station_battery_posts`: `FOCUS_FILTER_AIR_XP` added by focus audit subagent.
- `ukr_soviet_collapse_black_sea_port_ledgers`: `FOCUS_FILTER_NAVY_XP`
- `internal_soviet_collapse_peninsula_fortress_plan`: `FOCUS_FILTER_AIR_XP`
- `internal_soviet_collapse_far_eastern_port_authority`: `FOCUS_FILTER_NAVY_XP`
- `internal_soviet_collapse_pacific_harbor_guard`: `FOCUS_FILTER_AIR_XP`, `FOCUS_FILTER_NAVY_XP`
- `kaz_soviet_collapse_airstrips_on_the_steppe`: `FOCUS_FILTER_AIR_XP`
- `kaz_soviet_collapse_army_of_the_open_horizon`: `FOCUS_FILTER_AIR_XP`
- `kaz_soviet_collapse_iranian_caspian_notes`: `FOCUS_FILTER_NAVY_XP`
- `NRF_living_harbor_committees`: `FOCUS_FILTER_NAVY_XP`
- `NRF_letters_to_sailor_towns`: `FOCUS_FILTER_NAVY_XP`
- `NRF_memorial_convoy_state`: `FOCUS_FILTER_NAVY_XP`
- `ARD_murmansk_dockyard_sheds`: `FOCUS_FILTER_NAVY_XP`
- `ARD_white_sea_customs`: `FOCUS_FILTER_NAVY_XP`
- `ARD_foreign_fleet_letters`: `FOCUS_FILTER_NAVY_XP`
- `ARD_white_sea_port_tolls`: `FOCUS_FILTER_NAVY_XP`
- `ARD_arctic_port_endurance`: `FOCUS_FILTER_NAVY_XP`

## Audit Results

- Direct focus completion-reward audit across the four Soviet Collapse focus files found:
  - `0` repeated direct Soviet Collapse helper calls inside a single focus reward.
  - `0` raw `add_ideas`, `remove_ideas`, or `swap_ideas` calls inside focus completion rewards after this patch.
- Recursive focus-helper audit found:
  - `0` focus rewards that can recursively add the same idea more than once through Soviet Collapse scripted effects.
- Mission/report events `chaosx.nr5.30` through `chaosx.nr5.49` already use `minor_flavor = yes` and `major = no`.
- Terminal/scenario release path currently calls repeated `every_possible_country` release passes through:
  - `soviet_collapse_release_terminal_all_ordinary_republics`
  - `soviet_collapse_force_terminal_all_possible_core_countries_exhaustive`
  - `soviet_collapse_free_terminal_soviet_subjects`
  - chaos-scenario gated `soviet_collapse_spawn_terminal_high_chaos_successors`

## Validation

- Brace balance checked for Event005 constants, focus files, scripted effects, decisions, events, and main localisation.
- `git diff --check` passed for the touched Event005 file set.
- Unsupported operator scan for `<=` and `>=` passed on the touched Event005 file set.
- No flag diffs:
  - `git diff --name-only | rg '(^|/)gfx/flags/|\.tga$|flag.*\.(gfx|dds|tga)$|(^|/)flags/' || true`
  - produced no output.

## Remaining Gaps

- The broader focus-tree depth rework is still incomplete. This tranche proves idea-spam cleanup for direct and recursively repeated focus rewards, but it does not prove every branch has the final requested political, industrial, military, diplomacy, expansion, and special-mechanic depth.
- Visual pathline cleanliness still needs the current focus audit subagent result plus parent review.
- Chaos country identity depth is improved in several helpers, but not every chaos country has been audited to the requested final standard.
