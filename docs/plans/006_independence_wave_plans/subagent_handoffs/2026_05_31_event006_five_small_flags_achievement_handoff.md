# Event 006 Five Small Flags Achievement Handoff

## Scope

Added the `cr_five_small_flags` custom achievement for the existing Event006 mutual-guarantee network mechanic.

No subagent was spawned for this tranche because the gameplay tracking, files, and asset scope were bounded and did not require new country flags.

## Files Changed

- `common/achievements/chaos_redux_achievements.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `interface/chaosx_achievements.gfx`
- `docs/events/006_independence_wave.md`
- `docs/assets/006_independence_wave/achievement_icons/manifest.md`
- `docs/assets/006_independence_wave/achievement_icons/prompts/cr_five_small_flags.txt`
- `docs/assets/006_independence_wave/achievement_icons/source_png/cr_five_small_flags_source.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags_grey.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_five_small_flags_not_eligible.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`
- `gfx/achievements/cr_five_small_flags.dds`
- `gfx/achievements/cr_five_small_flags_grey.dds`
- `gfx/achievements/cr_five_small_flags_not_eligible.dds`

## Implementation

- `cr_five_small_flags` checks Event006 origin, independent release status, a signed mutual-guarantee participant flag, `chaosx_iw_mutual_guarantee_network`, and the global mutual guarantee count against `constant:independence_wave_achievement.mutual_guarantee_network_required`.
- The faction gate allows no faction or the Event006 compact/League path and rejects being in faction with SOV, so it does not reward Soviet Collapse control.
- The achievement uses existing gameplay tracking from `independence_wave_sign_mutual_guarantee_effect`.
- `is_independence_wave_achievement_release` now explicitly rejects Soviet Collapse origin, Event005 republic, breakaway, and high-chaos successor flags for the whole Event006 achievement family.
- Localisation adds title, description, and tooltip text.
- Achievement sprites are registered in `interface/chaosx_achievements.gfx`.
- The icon triplet uses generic symbolic banners over a congress ledger, not real country flags.

## Validation

- Final DDS files identify as 64x64 ARGB8888.
- The achievement references an existing script constant and existing Event006 mutual-guarantee flags.
- No country files, history files, or country flag assets were edited.

## Remaining Risks

- This closes only the mutual-guarantee achievement gap. League-war, human-renunciation, and final-settlement achievement clusters remain follow-up work.
