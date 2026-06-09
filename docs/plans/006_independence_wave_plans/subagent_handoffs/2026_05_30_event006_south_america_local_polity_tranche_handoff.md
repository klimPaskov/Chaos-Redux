# Event 006 South America Local-Polity Tranche Handoff

## Scope

Implemented two verified Event 006 local-polity starter packages for the Evo IV package ladder without touching flag assets, country files, or history files.

- `GAR` Guarani Land Congress package.
- `CHR` Charrua Assembly package.
- Both use vanilla-supported tags and vanilla core precedents.
- Both use reduced-release anchors so host survival still overrides release count.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`

## Implementation details

- Added high-chaos seed gates for `GAR` and `CHR` that require weak, surrendering, or wartime hosts and more than the configured host-survival floor.
- Seeded vanilla Guarani and Charrua core sets inside the Event 006 package resolver before candidate scoring.
- Added package scoring flags, package ids, land-congress formation family, local-polity classification, and package national spirits.
- Added bespoke reduced-release anchor preferences:
  - Guarani: `510`, `502`, `688`.
  - Charrua: `945`, `946`.
- Added package focuses under `independence_wave_land_congress_clue`.
- Added Formation Ledger decisions and post-formation integration missions.
- Added package and formation event-log row constants, record effects, scripted localisation routing, and GUI localisation labels.
- Updated local-polity AI strategy detection for the new package flags and formation states.
- Updated Event 006 documentation, including asset handoff names for later custom art.

## Vanilla evidence

- `GAR` and `CHR` are vanilla tags in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Vanilla history files define Guarani and Charrua country cores.
- Vanilla MTG Chile on-action content adds Guarani and Charrua cores and transfers the same state families, which supports the state selections used here.

## Validation

- Brace balance passed for all touched Event 006 script files and `chaosx_scripted_localisation_events_log.txt`.
- `rg "<=|>="` found no unsupported comparison operators in touched files.
- `git diff --check` passed for tracked changes.
- Localisation BOM checks passed for both touched localisation files.
- No `:0` localisation keys were introduced.
- Trailing-whitespace/final-newline check passed for touched files.
- `git status --short -- gfx/flags common/countries history/countries` returned no touched flag/country/history paths.

## Remaining work

- No custom package icons or idea art were created. The docs reserve stable `GFX_*` names for later art handoff.
- No custom leaders, portraits, or flag work was performed.
- The broader Event 006 source spec remains incomplete; this tranche only closes one package-count gap in the Evo IV local-polity ladder.
