# Event 006 Host-Survival Achievement Tranche Handoff

## Scope

Implemented two additional Event 006 achievement definitions and release-chain tracking for host survival outcomes. This tranche does not touch flag assets, country definitions, history files, or Event 005 Soviet Collapse systems.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `events/006_independence_wave.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `localisation/english/chaosx_achievements_l_english.yml`
- `interface/chaosx_achievements.gfx`
- `docs/events/006_independence_wave.md`

## Identifiers

- Achievements:
  - `cr_capital_still_answers`
- Tracking flags:
  - `chaosx_iw_capital_still_answers`
  - `chaosx_iw_mass_wave_hosts_survived`
- Variables:
  - `global.independence_wave_wave_serial`
  - `global.chaosx_iw_current_wave_host_count`
  - `independence_wave_host_counted_wave_id`
  - `independence_wave_host_current_wave_release_loss_count`
- Constants:
  - `independence_wave_achievement.capital_survival_release_losses_required`
  - `independence_wave_achievement.mass_wave_release_count_required`
  - `independence_wave_achievement.mass_wave_host_count_required`

## Behavior

- `cr_capital_still_answers` unlocks for a host that remains in Event 006 aftermath, keeps ownership and control of its capital, and has endured at least four counted Event 006 release rounds in the same wave.
- Host counting uses a per-wave serial variable on affected hosts, so one host is counted once per wave even if multiple releases are carved away from it.

## Asset Handoff

`chaosx_icon_artist` produced final achievement icon triplets for both achievements under `gfx/achievements/` and `docs/assets/006_independence_wave/achievement_icons/`; see `2026-05-30_event_006_achievement_icons.md`.

Final DDS files:

- `gfx/achievements/cr_capital_still_answers.dds`
- `gfx/achievements/cr_capital_still_answers_grey.dds`
- `gfx/achievements/cr_capital_still_answers_not_eligible.dds`

Parent validation confirmed the active DDS files and processed PNG files are `64x64`. The review contact sheet shows no flag imagery.

## Validation

- Static brace-balance validation passed for Event 006 constants, scripted effects, event file, achievements, and achievement GFX.
- Checked the bounded tranche files for unsupported `<=` / `>=`; none found.
- `localisation/english/chaosx_achievements_l_english.yml` and `localisation/english/006_independence_wave_l_english.yml` remain UTF-8 with BOM and have no `:0` keys.
- `git status --short -- gfx/flags common/countries history/countries` returned no changes.

## Remaining Risks

- This uses release rounds as the severe-host-loss proof because the current reduced-release resolver intentionally releases conservative anchor territory before later claim work.
- Runtime UI validation was not performed.
- This tranche does not implement strange-state, league-war, human-renunciation, or final-settlement achievements.
