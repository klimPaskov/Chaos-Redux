# Event006 Mapuche Package Parent Handoff

## Summary

- Added custom Event 006 country tag `MAP` for the Mapuche Land Congress.
- Implemented `MAP` as a high-chaos local-polity package, not a Chile cosmetic fallback and not a bespoke focus-tree stack.
- Release anchor: Araucania `950`.
- Later expansion territory: Aysen `949` and Rio Negro `512` become surveyed cores through Mapuche petition work so the shared Border Commission recovery path can transfer them if the target owner survives.

## Changed Files

- `common/country_tags/chaosx_countries.txt`
- `common/countries/Mapuche Land Congress.txt`
- `history/countries/MAP - Mapuche Land Congress.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

## Asset Handoff Reviewed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_175813_event006_mapuche_flag_asset_handoff.md`
- `docs/assets/006_independence_wave/flags/mapuche/manifest.md`
- Final files:
  - `gfx/flags/MAP.tga`
  - `gfx/flags/medium/MAP.tga`
  - `gfx/flags/small/MAP.tga`

## Validation

- Brace balance passed for touched script files.
- No unsupported comparison operators found in touched script files.
- No trailing whitespace or CRLF found in touched files.
- Localisation BOM check passed for touched localisation files.
- `identify`/`file` validation confirmed MAP flags are 82x52, 41x26, and 10x7 RGBA TGA files with `TopLeft` orientation.

## Remaining Risks

- MAP uses a vanilla generic South American portrait rather than a bespoke sourced portrait.
- MAP uses the shared Event 006 provisional focus tree by design; package identity is expressed through decisions, variables, idea, country setup, and localisation.
- Final Event 006 completion audit is still required before any full completion claim.
