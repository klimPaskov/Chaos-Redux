# Event 006 release list and evolution milestone patch

## Scope

Parent patch for the urgent Event 006 report that the Independence Wave news release list was colored and that release-scale evolution milestones were still missing.

## Changes

- `localisation/english/006_independence_wave_l_english.yml`
  - Removed yellow formatting wrappers from `independence_wave_released_country_list_1` through `independence_wave_released_country_list_16`.
  - The confirmed-release names now display in normal text color inside `chaosx.news.6.d`.

- `common/scripted_effects/006_independence_wave_effects.txt`
  - `independence_wave_prepare_release_count` now stores the resolved release-scale milestone in `global.independence_wave_release_scale_stage`.
  - `independence_wave_record_tier_evolution_log_entry` now records the four real Event 006 release-scale milestones from the resolved stage plus the chaos tier:
    - Gathering Storm
    - Rising Cascade
    - Old Names Return
    - Impossible Statehood
  - Baseline calm-world waves still do not write evolution rows.
  - The recorder uses new milestone flags while also setting the older compatibility flags, so saves that already received old broken test flags can still write the repaired milestone row once.
  - Each milestone respects `is_current_evolution_enabled = yes` after setting the stage temp variable needed by the setting trigger.

- `docs/events/006_independence_wave.md`
  - Documented `global.independence_wave_release_scale_stage` and the exact four milestone rows.

## Validation

- Brace balance:
  - `common/scripted_effects/006_independence_wave_effects.txt`: `balance=0 min=0`
  - `events/006_independence_wave.txt`: `balance=0 min=0`
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: `balance=0 min=0`
  - `common/script_constants/006_independence_wave_constants.txt`: `balance=0 min=0`
- Unsupported operators: no forbidden less-than-or-equal or greater-than-or-equal operators found in touched Event 006 files.
- Localisation encoding: `localisation/english/006_independence_wave_l_english.yml` starts with UTF-8 BOM `efbbbf`.
- Release-list color check: no `§Y[?global.independence_wave_country_` matches remain.
- `git diff --check` clean for the touched files.

## Remaining risk

The new milestone flags intentionally permit one repaired milestone row in saves where the older `independence_wave_evolution_*_logged` flags were already set by prior broken testing. On a save that already had visible milestone rows, this can create one duplicate per stage after the patch, but it is capped to the four real Event 006 milestones and will not create per-release entries.
