# Event 006 Achievement Tranche Handoff

Date: 2026-05-30

## Scope

Implemented the first actual Event 006 custom-achievement tranche for Independence Wave systems that already have gameplay hooks. This tranche does not claim full Event 006 completion.

No flags, flag definitions, flag images, or flag assets were edited. No Event 005 mechanics were edited for this tranche.

## Files changed

- `common/achievements/chaos_redux_achievements.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/systems/custom_achievements.md`
- `docs/assets/006_independence_wave/achievement_icons/`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_achievement_icons_handoff.md`

The icon subagent also created commit `1ce8f5bf` with the generated icon package only.

## Achievement ids added

- `cr_brokers_exposed`
- `cr_partition_without_war`
- `cr_first_old_name`
- `cr_local_land_congress`
- `cr_railway_country`
- `cr_not_the_collapse`
- `cr_charter_becomes_state`
- `cr_the_ledger_votes_back`

## Script behavior added

- Added reusable Event 006 achievement guard triggers:
  - `is_independence_wave_achievement_clean`
  - `is_independence_wave_achievement_release`
  - `is_independence_wave_achievement_independent_release`
- Added achievement constants for peaceful Border Commission count and League-member count.
- Added first historical-return package tracking through `chaosx_iw_first_old_name_seen` and `chaosx_iw_first_old_name_country`.
- Added a country-side peaceful Border Commission counter for arbitration, protected transfer petitions, and observer freezes.
- Added `independence_wave_dossier_ultimatum_issued` as a country flag when the ultimatum path is used, so `cr_partition_without_war` has a real disqualifier.
- Added GFX sprite aliases for every Event 006 achievement icon triplet.
- Added achievement localisation and custom achievement documentation.

## Icon package

Icon subagent: `chaosx_icon_artist`

Handoff:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_achievement_icons_handoff.md`

Manifest:

- `docs/assets/006_independence_wave/achievement_icons/manifest.md`

The package created DDS triplets for all eight achievement ids under `gfx/achievements/`.

## Validation

- Brace balance is clean for:
  - `common/achievements/chaos_redux_achievements.txt`
  - `interface/chaosx_achievements.gfx`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `events/006_independence_wave.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
- Unsupported pattern scan found no `<=`, `>=`, direct constant duration fields, or unary negative variable-token assignments in the checked Event 006/achievement files.
- `localisation/english/chaosx_achievements_l_english.yml` and `localisation/english/006_independence_wave_l_english.yml` both retain UTF-8 BOM.
- No `:0` localisation keys were found in the checked achievement/Event 006 localisation files.
- `git diff --check` passed for the touched script, localisation, GFX, docs, manifest, and handoff files.
- Parent-side alignment check confirmed every new achievement id has:
  - an achievement definition
  - `_NAME`, `_DESC`, and `_tooltip` localisation
  - three GFX aliases
  - three DDS files at the referenced paths
- Visual contact sheet was reviewed for the eight final icons.

## Skipped validation

- No in-game achievement unlock test was run.
- No live HOI4 UI render test was run.
- No flag or flag-asset validation was run because this tranche did not touch flags or flag assets.

## Remaining blockers

- Event 006 still lacks the full requested achievement catalog. Host-survival, mass-wave, league-war, impossible-state, human-renunciation, and final-settlement achievements remain unimplemented because their supporting gameplay surfaces are incomplete or missing.
- Super-events, final asset pack coverage, scripted GUI surfaces, strange/containment packages, and reduced-territory release handling remain blockers for full Event 006 completion.
- The icon package uses ImageMagick-generated RGB888 DDS output. The files validate on disk and match the existing achievement dimensions, but they may need reconversion if the project later standardizes on a stricter DDS encoder.
