# Event006 Old Name Modern State Achievement Handoff

## Scope

Implemented the Event 006 `cr_old_name_modern_state` achievement and its achievement icon triplet. No country definitions, country history, country flag assets, or Event 005 files were edited.

## Changed files

- `common/achievements/chaos_redux_achievements.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/systems/custom_achievements.md`
- `docs/assets/006_independence_wave/achievement_icons/manifest.md`
- `docs/assets/006_independence_wave/achievement_icons/prompts/cr_old_name_modern_state.txt`
- `docs/assets/006_independence_wave/achievement_icons/source_png/cr_old_name_modern_state_source.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state_grey.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_old_name_modern_state_not_eligible.png`
- `gfx/achievements/cr_old_name_modern_state.dds`
- `gfx/achievements/cr_old_name_modern_state_grey.dds`
- `gfx/achievements/cr_old_name_modern_state_not_eligible.dds`

## Behavior

- Added achievement id `cr_old_name_modern_state`.
- Requires an independent Event 006 release, historical-return package tracking, Event 006 formation origin, and completion of either Volga-Kama ministry integration or Assyrian recognition congress integration.
- Disqualifies Event 005/Soviet Collapse origin and puppet history through `is_independence_wave_achievement_independent_release`.
- Disqualifies the implemented offensive border-war escalation surrogate by rejecting `independence_wave_dossier_ultimatum_issued`.

## Assets

- Registered `GFX_achievement_cr_old_name_modern_state` and its grey/not-eligible variants in `interface/chaosx_achievements.gfx`.
- Created 64x64 DDS triplet in `gfx/achievements/`.
- Source art is generated-derived from existing Event006 old-name and charter source images because the live image generation tool did not expose the newly generated image as a local file.

## Validation

- Brace balance passed for `common/achievements/chaos_redux_achievements.txt` and `interface/chaosx_achievements.gfx`.
- Unsupported-operator scan passed for touched script, interface, localisation, and docs surfaces.
- `localisation/english/chaosx_achievements_l_english.yml` remains UTF-8 with BOM and has no `:0` localisation keys.
- Achievement DDS triplet exists and validates as `64 x 64` RGB888.
- `git diff --check` passed.

## Remaining work

- This closes only the modern old-name achievement gap. League-war, human-renunciation, and final-settlement achievement clusters remain follow-up work.
