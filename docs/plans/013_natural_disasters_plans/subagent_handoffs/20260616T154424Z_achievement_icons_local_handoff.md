# Event 013 Achievement Icons Local Handoff

Worker: main agent local asset pass.

Reason: a new `chaosx_icon_artist` achievement-icon subagent could not be spawned because the active thread hit the agent concurrency limit. Existing Event 013 generated-art sources were available, so the achievement package was produced locally instead of leaving the achievement UI unwired.

## Outputs

- Source PNGs: `docs/assets/013_natural_disasters/achievement_icons/source_png/`
- Processed PNGs: `docs/assets/013_natural_disasters/achievement_icons/processed_png/`
- Contact sheet: `docs/assets/013_natural_disasters/achievement_icons/ACH_ND_contact_sheet.png`
- Final DDS files: `gfx/achievements/ACH_ND_*.dds`, `gfx/achievements/ACH_ND_*_grey.dds`, and `gfx/achievements/ACH_ND_*_not_eligible.dds`
- Manifest: `docs/assets/013_natural_disasters/achievement_icons/manifest.md`
- Sprite registration: `interface/chaosx_achievements.gfx`

## Registered IDs

- `ACH_ND_RING_THE_BELL`
- `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
- `ACH_ND_THE_TRAINS_ARRIVED`
- `ACH_ND_NO_PORT_LEFT_BEHIND`
- `ACH_ND_GRAIN_AGAINST_THE_DUST`
- `ACH_ND_ASH_ON_THE_RUNWAY`
- `ACH_ND_SKY_ARTILLERY_SURVIVOR`
- `ACH_ND_THE_SEA_WALKED_BACK`
- `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
- `ACH_ND_DISASTER_LEDGER_CLOSED`
- `ACH_ND_NO_WORLD_END_REQUIRED`
- `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`

## Notes

- Final assets keep the exact achievement ID stems expected by the Chaos Redux custom achievement UI.
- All icons have normal, grey, and not-eligible variants.
- The package is replacement-safe: future art can overwrite the same final DDS filenames without changing script or localisation IDs.
