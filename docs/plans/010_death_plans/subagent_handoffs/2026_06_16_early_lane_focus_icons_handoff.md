# Event 010 Death early-lane focus icon handoff

Date: `2026-06-16`
Scope: regenerate only the assigned 10 early-lane Death national focus icons as distinct HOI4-style focus art

## Rejection note

- The previous early-lane batch with the repeated bell/medallion motif was rejected.
- That repeated-bell batch has been replaced in this handoff with 10 distinct source compositions and fresh processed outputs.

## Files changed

- `docs/assets/010_death/source_png/focus_death_the_first_silence_source.png`
- `docs/assets/010_death/source_png/focus_death_country_on_the_island_source.png`
- `docs/assets/010_death/source_png/focus_death_shroud_whispers_source.png`
- `docs/assets/010_death/source_png/focus_death_no_mail_before_spring_source.png`
- `docs/assets/010_death/source_png/focus_death_weather_on_paper_source.png`
- `docs/assets/010_death/source_png/focus_death_island_pattern_source.png`
- `docs/assets/010_death/source_png/focus_death_hunger_shore_source.png`
- `docs/assets/010_death/source_png/focus_death_lowest_names_first_source.png`
- `docs/assets/010_death/source_png/focus_death_ports_without_voices_source.png`
- `docs/assets/010_death/source_png/focus_death_mainland_smell_source.png`
- `docs/assets/010_death/processed_png/focus_death_the_first_silence.png`
- `docs/assets/010_death/processed_png/focus_death_country_on_the_island.png`
- `docs/assets/010_death/processed_png/focus_death_shroud_whispers.png`
- `docs/assets/010_death/processed_png/focus_death_no_mail_before_spring.png`
- `docs/assets/010_death/processed_png/focus_death_weather_on_paper.png`
- `docs/assets/010_death/processed_png/focus_death_island_pattern.png`
- `docs/assets/010_death/processed_png/focus_death_hunger_shore.png`
- `docs/assets/010_death/processed_png/focus_death_lowest_names_first.png`
- `docs/assets/010_death/processed_png/focus_death_ports_without_voices.png`
- `docs/assets/010_death/processed_png/focus_death_mainland_smell.png`
- `gfx/interface/goals/death/focus_death_the_first_silence.dds`
- `gfx/interface/goals/death/focus_death_country_on_the_island.dds`
- `gfx/interface/goals/death/focus_death_shroud_whispers.dds`
- `gfx/interface/goals/death/focus_death_no_mail_before_spring.dds`
- `gfx/interface/goals/death/focus_death_weather_on_paper.dds`
- `gfx/interface/goals/death/focus_death_island_pattern.dds`
- `gfx/interface/goals/death/focus_death_hunger_shore.dds`
- `gfx/interface/goals/death/focus_death_lowest_names_first.dds`
- `gfx/interface/goals/death/focus_death_ports_without_voices.dds`
- `gfx/interface/goals/death/focus_death_mainland_smell.dds`
- `docs/assets/010_death/contact_sheets/death_focus_icons_early_lane_contact.png`

## Subject summary

- `focus_death_the_first_silence`: abandoned island signal room and silent radio mast
- `focus_death_country_on_the_island`: black island office and black flag silhouette
- `focus_death_shroud_whispers`: fogged receiver and shadowed telegraph-wire signal motif
- `focus_death_no_mail_before_spring`: abandoned dock mailbag and unopened letters
- `focus_death_weather_on_paper`: storm report papers and barometer misdirection
- `focus_death_island_pattern`: archipelago chart with black island dots and route pins
- `focus_death_hunger_shore`: black shoreline swallowing a broken pier
- `focus_death_lowest_names_first`: census ledger with small name tabs and registry cards
- `focus_death_ports_without_voices`: empty harbor crane, signal horn, and port radio shape
- `focus_death_mainland_smell`: distant continental coastline with inland road hint

## Validation

- Verified all 10 source PNGs exist at the stable source paths.
- Verified all 10 processed PNGs exist and are exactly `94x86`.
- Verified all 10 final DDS files exist and are exactly `94x86`.
- Verified the early-lane contact sheet exists at `docs/assets/010_death/contact_sheets/death_focus_icons_early_lane_contact.png`.
- Verified the current source PNG set and the fresh contact-sheet render show distinct subjects rather than the rejected repeated-bell motif.

## Blockers

- None in this early-lane batch.

## Intentionally untouched

- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/generated_art_gfx_handoff.md`
- Shared all-icons Death focus contact sheets outside this early-lane batch
- Gameplay, localisation, `.gfx`, focus tree, and script files
