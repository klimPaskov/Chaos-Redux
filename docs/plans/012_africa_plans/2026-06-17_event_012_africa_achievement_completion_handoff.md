# Event 012 Africa Achievement Completion Handoff

## Scope

Parent implementation pass after the completion auditor flagged achievement-prompt coverage as incomplete or undispositioned.

Gameplay files touched:

- `common/script_constants/achievement_constants.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `docs/events/012_africa_foundation.md`

Asset subagent work landed in `docs/assets/012_africa/achievement_icons_prompt_completion_batch_4/`, `docs/assets/012_africa/achievement_icons_prompt_completion_batch_5/`, `docs/assets/012_africa/achievement_icons_prompt_completion_batch_6/`, and live `gfx/achievements/ACH_AFR_*.dds`.

## Implemented achievement coverage

Existing Event 012 achievements remained intact. The pass added prompt-completion achievements for:

- `ACH_AFR_THE_ALLIES_SIGN`
- `ACH_AFR_ELEPHANTS_REMEMBER`
- `ACH_AFR_ANANSE_WROTE_THE_ORDERS`
- `ACH_AFR_TIDE_TOOK_THE_PORT`
- `ACH_AFR_FOREST_GUARDIAN_PACT`
- `ACH_AFR_BIGGER_CARAVAN`
- `ACH_AFR_NOT_A_MAP_COLOUR`
- `ACH_AFR_CONGRESS_OVER_COMMAND`
- `ACH_AFR_COMMAND_OVER_CONGRESS`
- `ACH_AFR_OLD_THRONES_VOTE`
- `ACH_AFR_EVERY_CAPITAL_HEARD_THE_DRUM`
- `ACH_AFR_WORLD_SCHOOL`
- `ACH_AFR_AFRO_ASIAN_VECTOR`
- `ACH_AFR_AFRO_EURASIAN_QUESTION`
- `ACH_AFR_WORLD_IS_ONE`
- `ACH_AFR_NO_FALSE_BEASTS`
- `ACH_AFR_FOREST_VOTES_NO`
- `ACH_AFR_NO_IVORY_TREASURY`
- `ACH_AFR_TREATY_WITH_TEETH`
- `ACH_AFR_WORLD_HAS_ROOTS`
- `ACH_AFR_SMALL_THRONES_SIT_TOGETHER`
- `ACH_AFR_NO_MAP_CAN_HOLD_THIS`
- `ACH_AFR_WALKING_WALLS`
- `ACH_AFR_ARCHIVE_UNBROKEN`
- `ACH_AFR_CORAL_ADMIRALTY`
- `ACH_AFR_KUOMBOKA_ARMY`

These entries use existing Event 012 route flags, mission-success flags, Bestiary action flags, dynamic union identity flags, continent-unifier proof flags, and live variables. They do not unlock on Event 012 fire alone.

## Queued achievement designs

The following prompt/spec rows remain queued because their exact actor packages do not exist in the implemented Event 012 surface:

- Hyena Radio Dominion / `africa_who_gave_them_a_microphone`
- Bonobo Kinship Congress / `africa_gentle_veto`
- Bird of the Walls / `africa_bird_was_right`
- Sao Terracotta Host / `ACH_AFRICA_TERRACOTTA_LINE`

These should be implemented only after the corresponding actor/country packages, flags, route decisions, and assets exist. They were not faked through unrelated Bestiary actors.

## Validation notes

- Achievement thresholds added under `achievement_threshold.africa` for all-regional-authority, archive-survival, high-chaos-pact, cohesion, warning-compliance, and sponsor-count checks.
- Localisation uses stable `ACH_AFR_*_NAME`, `ACH_AFR_*_DESC`, and `ACH_AFR_*_tooltip` keys.
- The 26 new achievement families have live normal, `_grey`, and `_not_eligible` DDS variants and are registered in `interface/chaosx_achievements.gfx`.
