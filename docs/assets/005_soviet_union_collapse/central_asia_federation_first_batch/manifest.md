## Event 005 Central Asia Federation First Batch

Event id: `005`

Event slug: `soviet_union_collapse`

Asset type: focus icons

Intended in-game use: unique replacements for the four-focus duplicate group currently sharing `GFX_central_asia_soviet_collapse_steppe_federation`

Source mode: `$imagegen` generated symbolic focus-icon art on fake-checker transparency output, alpha-cleaned with ImageMagick flood-fill corner removal, resized to `94x86`, converted to DDS with `convert -define dds:compression=none`

Reference folders inspected:

- `.agents/skills/chaos-redux-event-assets/assets/focuses/`
- existing Event 005 shared sprites converted for local inspection:
  - `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_steppe_federation.dds`
  - `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_rail_and_irrigation_boards.dds`

Current duplicate source audited:

- `common/national_focus/005_soviet_collapse_republics.txt:6394`
- `common/national_focus/005_soviet_collapse_republics.txt:6640`
- `common/national_focus/005_soviet_collapse_republics.txt:6662`
- `common/national_focus/005_soviet_collapse_republics.txt:6881`
- `interface/005_soviet_collapse_regional_icons.gfx:372`

Produced icons:

| Focus | Proposed sprite | Source PNG | Processed PNG | Final package DDS | Final root DDS | Target size | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `central_asia_soviet_collapse_turkestan_city_congress` | `GFX_central_asia_soviet_collapse_turkestan_city_congress` | `source_png/central_asia_soviet_collapse_turkestan_city_congress_source.png` | `processed_png/central_asia_soviet_collapse_turkestan_city_congress.png` | `package_dds/central_asia_soviet_collapse_turkestan_city_congress.dds` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_city_congress.dds` | `94x86` | `needs_user_review` | Alpha is real in processed/root DDS, but cleanup came from checkerboard flood-fill rather than true source alpha. |
| `central_asia_soviet_collapse_turkestan_federation_road` | `GFX_central_asia_soviet_collapse_turkestan_federation_road` | `source_png/central_asia_soviet_collapse_turkestan_federation_road_source.png` | `processed_png/central_asia_soviet_collapse_turkestan_federation_road.png` | `package_dds/central_asia_soviet_collapse_turkestan_federation_road.dds` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_federation_road.dds` | `94x86` | `needs_user_review` | Same alpha-cleanup caveat. |
| `central_asia_soviet_collapse_federation_delegates` | `GFX_central_asia_soviet_collapse_federation_delegates` | `source_png/central_asia_soviet_collapse_federation_delegates_source.png` | `processed_png/central_asia_soviet_collapse_federation_delegates.png` | `package_dds/central_asia_soviet_collapse_federation_delegates.dds` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_delegates.dds` | `94x86` | `needs_user_review` | Same alpha-cleanup caveat. |
| `central_asia_soviet_collapse_federation_state` | `GFX_central_asia_soviet_collapse_federation_state` | `source_png/central_asia_soviet_collapse_federation_state_source.png` | `processed_png/central_asia_soviet_collapse_federation_state.png` | `package_dds/central_asia_soviet_collapse_federation_state.dds` | `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_state.dds` | `94x86` | `needs_user_review` | Same alpha-cleanup caveat. |

Validation summary:

- `identify` confirms every processed PNG and DDS is `94x86`
- `identify -verbose` reports `TrueColorAlpha` for all four root DDS files
- checker contact sheet written to `contact_sheets/central_asia_federation_first_batch_checker.png`
- no `.gfx` or focus wiring was changed here

Suggested target `.gfx` file:

- `interface/005_soviet_collapse_regional_icons.gfx`

Related duplicate group to replace:

- current shared sprite: `GFX_central_asia_soviet_collapse_steppe_federation`
- current shared texture: `gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_steppe_federation.dds`

