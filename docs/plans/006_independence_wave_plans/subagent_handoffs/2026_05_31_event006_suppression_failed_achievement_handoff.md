# Event 006 Suppression Failed Achievement Handoff

## Scope

Added the `cr_suppression_failed` custom achievement for the existing Event006 host hardline-response loop.

No subagent was spawned for this tranche because the gameplay surface was already implemented in host Dossier Board decisions and did not require new country flags.

## Files Changed

- `common/achievements/chaos_redux_achievements.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/systems/custom_achievements.md`
- `docs/assets/006_independence_wave/achievement_icons/manifest.md`
- `docs/assets/006_independence_wave/achievement_icons/prompts/cr_suppression_failed.txt`
- `docs/assets/006_independence_wave/achievement_icons/source_png/cr_suppression_failed_source.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed_grey.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_suppression_failed_not_eligible.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`
- `gfx/achievements/cr_suppression_failed.dds`
- `gfx/achievements/cr_suppression_failed_grey.dds`
- `gfx/achievements/cr_suppression_failed_not_eligible.dds`

## Implementation

- Added `constant:independence_wave_achievement.suppression_later_release_losses_required = 2`.
- Added `independence_wave_mark_host_suppression_for_achievements`, called by courier arrests and loyalist-council arming.
- Host aftermath marks `chaosx_iw_later_breakaways_lost_by_host` only when a later wave hits the same host for at least two additional releases.
- `cr_suppression_failed` checks clean achievement state, recent host status, the suppression setup flag, the later-breakaway flag, and the current wave release-loss count.
- Localisation adds title, description, and tooltip text.
- Achievement sprites are registered in `interface/chaosx_achievements.gfx`.

## Validation

- The achievement relies on existing Event006 host decisions and release-chain host counters.
- Final DDS files identify as 64x64 ARGB8888.
- No Event005 files, country files, history files, or country flag assets were edited.

## Remaining Risks

- This closes only the host-suppression achievement gap. Modern old-name, league-war, human-renunciation, and final-settlement achievement clusters remain follow-up work.
