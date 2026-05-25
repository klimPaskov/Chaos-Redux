# Event 005 Generated Event Art Handoff

Scope: Event 005 Soviet Collapse fictional leader/council portraits and fictional custom-country or route flags only.

## Handoff result

No new sprite definitions or `.gfx` edits are needed from this sidecar.

Active fictional/council leader portraits already exist as final DDS files in `gfx/leaders/005_soviet_collapse/` and match the existing country-history portrait references. Active custom-country flags already exist in normal, medium, and small TGA folders with the expected HOI4 dimensions.

## Wiring notes

- Keep existing portrait sprite names from the country-history files, such as `GFX_portrait_CFR_construction_board`, `GFX_portrait_MFR_arsenal_board`, and the corresponding Event 005 custom-country portrait names.
- Keep existing flag filenames for Event 005 custom tags: base plus `_communism`, `_democratic`, `_fascism`, and `_neutrality`.
- Do not wire generated default base-flag overrides for existing in-game countries. Existing-country route changes should remain explicit route or cosmetic-tag assets.

## Blocked assets

No active scoped leader/council/flag asset is blocked.

Inactive or stale families such as `BEC`, `BLT`, `COU`, `ILU`, and `IRA` should only receive new generated council portraits or flag families if a parent task restores them to active country-package use.
