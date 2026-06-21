# Event 012 Africa Idea Icon Validation Summary

Validation target: the 12 prompt-listed idea ids from `docs/specs/012_africa_specs/prompts/012_africa_asset_prompt.md`

## Live DDS Validation

All 12 prompt-listed live DDS files decode at `64x64`. Every decoded DDS has:

- all four corner pixels fully transparent
- `transparent_nonblack_pixels = 0`
- `transparent_white_pixels = 0`
- `opaque_square = false`

Newly generated assets validated in this package:

| Asset id | Live DDS path | Alpha bounds | Result |
| --- | --- | --- | --- |
| `idea_africa_paper_cores` | `gfx/interface/ideas/012_africa/idea_africa_paper_cores.dds` | `(3, 3, 60, 61)` | `ok` |
| `idea_africa_proclamation_without_machinery` | `gfx/interface/ideas/012_africa/idea_africa_proclamation_without_machinery.dds` | `(3, 4, 61, 60)` | `ok` |
| `idea_africa_regional_trust` | `gfx/interface/ideas/012_africa/idea_africa_regional_trust.dds` | `(6, 3, 57, 61)` | `ok` |
| `idea_africa_colonial_alarm` | `gfx/interface/ideas/012_africa/idea_africa_colonial_alarm.dds` | `(7, 3, 57, 61)` | `ok` |
| `idea_africa_liberation_momentum` | `gfx/interface/ideas/012_africa/idea_africa_liberation_momentum.dds` | `(3, 4, 61, 60)` | `ok` |
| `idea_africa_congress_legitimacy` | `gfx/interface/ideas/012_africa/idea_africa_congress_legitimacy.dds` | `(3, 3, 60, 61)` | `ok` |
| `idea_africa_continental_general_staff` | `gfx/interface/ideas/012_africa/idea_africa_continental_general_staff.dds` | `(3, 3, 60, 61)` | `ok` |
| `idea_africa_green_covenant` | `gfx/interface/ideas/012_africa/idea_africa_green_covenant.dds` | `(10, 3, 54, 61)` | `ok` |
| `idea_africa_diaspora_return_cadres` | `gfx/interface/ideas/012_africa/idea_africa_diaspora_return_cadres.dds` | `(3, 6, 61, 57)` | `ok` |
| `idea_africa_scramble_pressure` | `gfx/interface/ideas/012_africa/idea_africa_scramble_pressure.dds` | `(5, 3, 58, 61)` | `ok` |

Existing retained assets rechecked in the live folder:

| Asset id | Live DDS path | Alpha bounds | Result |
| --- | --- | --- | --- |
| `idea_africa_charter_league` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | `(10, 3, 54, 63)` | `ok` |
| `idea_africa_world_is_one_ambition` | `gfx/interface/ideas/012_africa/idea_africa_world_is_one_ambition.dds` | `(5, 3, 58, 61)` | `ok` |

## Idea-Versus-Goal Distinction Review

Distinctness proof sheet: `contact_sheets/idea_vs_goal_distinctness_pairs.png`

Reviewed pairings:

- `idea_africa_charter_league` vs `goal_africa_charter_league_emblem`
- `idea_africa_regional_trust` vs `goal_africa_regional_integration`
- `idea_africa_colonial_alarm` vs `goal_africa_scramble_for_africa`
- `idea_africa_liberation_momentum` vs `goal_africa_liberation_war_office`
- `idea_africa_congress_legitimacy` vs `goal_africa_political_congress`
- `idea_africa_continental_general_staff` vs `goal_africa_military_forces`
- `idea_africa_scramble_pressure` vs `goal_africa_scramble_for_africa`

Result:

- The newly generated idea icons are compact, idea-specific 64x64 emblems.
- They do not decode as resized, recolored, or cropped focus/goal icons.
- No opaque square background or white halo is present in the decoded live DDS outputs.
