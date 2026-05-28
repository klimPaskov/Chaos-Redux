# Event 005 Country Portrait/Name And Flag Audit

Date: 2026-05-28

Subagent scope: bounded country-package audit for Event 005 custom country leader portrait/name consistency and country flag file existence. No image files, gameplay scripts, focus trees, decisions, balance files, localisation, or `.gfx` files were edited.

Hard constraint applied: female-presenting one-person portraits must not receive male names and must set `female = yes` in direct `create_country_leader` blocks where supported. Male-presenting one-person portraits must not receive female names and must not set `female = yes`. Institutional or council portraits must keep institutional names and must not use random personal-name pools.

## Country Package Coverage Checklist

- Registered Event 005 custom tags audited from `common/country_tags/chaosx_countries.txt`: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`.
- Leader histories checked in `history/countries/<TAG> - *.txt`.
- Leader portrait sprite references checked through `interface/005_soviet_collapse*.gfx`.
- Random leader-name pools checked in `common/scripted_effects/005_soviet_collapse_effects.txt`, helper `soviet_collapse_randomize_single_person_leader_name`.
- Country flag files checked under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` for base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`.

## File Surface Checklist

- Read: `AGENTS.md`.
- Read: `.agents/skills/chaos-redux-events/SKILL.md`.
- Read: `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- Read: `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Read offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Portrait modding, Graphical asset modding, Ideology modding.
- Read vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`.
- Read vanilla precedents: vanilla `common/characters/` and `history/countries/` leader/character setup examples plus vanilla `gfx/flags/` and `gfx/leaders/` paths.
- Wrote: this handoff only.

## Missing Or Stale Country Package Surfaces

- No missing registered Event 005 custom country history file was found for the bounded tag set.
- No missing active leader portrait sprite definition was found for the bounded tag set.
- No missing active leader portrait texture file was found for the bounded tag set.
- No duplicate leader portrait SHA-256 hash was found among the registered Event 005 custom tag leader DDS files referenced by history.
- No missing base or ideology flag file was found for the registered Event 005 custom tag set in normal, medium, or small folders.
- Stale asset-manifest risk: the current audit found `gfx/flags/small/SOG*.tga` files exist but are 8 bpp color-mapped TGA files, while nearby Event 005 small flags are 32 bpp RGBA. Older asset notes claim the scoped small flags are 32 bpp. This is an asset-format risk, not an existence gap.

## Map And State Setup Issues

- Not audited by this bounded task. No map/state setup changes were made.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- Hard-blocker result:
  - No female-presenting one-person portrait in scope has a male name pool.
  - No male-presenting one-person portrait in scope has a female name pool.
  - No direct female-presenting one-person `create_country_leader` block in scope is missing `female = yes`.
  - No direct male-presenting one-person `create_country_leader` block in scope sets `female = yes`.
  - No portrait classified as institutional in the current active asset handoffs uses random personal-name pools.
- Female-presenting one-person leader histories are consistent:
  - `BAC`, `NLC`, `TSC`, `UDC`, and `UWD` each set `female = yes`, set `soviet_collapse_female_single_person_leader_portrait`, and call `soviet_collapse_randomize_single_person_leader_name = yes`.
  - The randomizer assigns only female pools for `BAC`, `NLC`, `TSC`, `UDC`, and `UWD`.
- Male-presenting one-person leader histories are consistent:
  - `ALA`, `ALN`, `ARD`, `BBH`, `BSC`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `MRC`, `NRF`, `OGB`, `PRA`, `RMC`, `SDZ`, `SOG`, `SZA`, and `TNC` set `soviet_collapse_male_single_person_leader_portrait`, call `soviet_collapse_randomize_single_person_leader_name = yes`, and do not set `female = yes`.
  - The randomizer assigns only male pools for those tags.
- Institutional leader portraits are consistent:
  - `CFR` uses `GFX_portrait_CFR_construction_board`, keeps `The Construction Board`, and does not call the personal-name randomizer.
  - `MFR` uses `GFX_portrait_MFR_arsenal_board`, keeps `The Arsenal Board`, and does not call the personal-name randomizer.
- Classification note:
  - The current active asset handoffs classify `SOG`, `ALN`, `KHW`, `KZR`, and `OGB` as male-presenting one-person portraits with background attendants/delegates, not institutional council portraits. Therefore their current male random personal-name pools satisfy the gender hard blocker. If an asset reviewer later classifies any of these as institutional/council portraits instead, their `soviet_collapse_randomize_single_person_leader_name = yes` calls must be removed before completion can be claimed.
- The recent parent correction is reflected:
  - `SOG`, `ALN`, `KHW`, `KZR`, and `OGB` use male portrait flags and male-only regional name pools.
- Flag existence result:
  - All 480 expected files exist for the 32 registered custom Event 005 tags: 32 tags x 5 variants x 3 sizes.
- Remaining flag risk:
  - `gfx/flags/small/SOG.tga`
  - `gfx/flags/small/SOG_communism.tga`
  - `gfx/flags/small/SOG_democratic.tga`
  - `gfx/flags/small/SOG_fascism.tga`
  - `gfx/flags/small/SOG_neutrality.tga`
  - These are present and correctly sized at `10x7`, but `file` reports them as 8 bpp color-mapped TGA files. Parent should decide whether to ask an asset subagent to re-export only these five small flags as vanilla-compatible 32 bpp RGBA TGAs.

## Focus, Decision, Idea, And Asset Issues

- Focuses, decisions, ideas, and balance scripts were intentionally not audited or edited.
- Asset existence checked only for active leader DDS paths referenced by history sprites and country flag TGA paths for the registered custom tags.
- No image files were generated, converted, rewritten, or moved.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Not audited by this bounded task. No military, technology, industry, supply, or production setup changes were made.

## AI And Playability Issues

- Not audited by this bounded task. No AI strategy, focus AI, decision AI, or playability balance files were edited.

## Validation Run

- `python3` registered-tag flag existence audit:
  - Result: `event005_tags 32 ...`
  - Result: `missing_count 0`
- `python3` leader metadata and sprite/texture audit:
  - Result: `classification_counts male 25 female 5 institutional 2`
  - Result: `metadata_issues 0`
  - Result: direct `female = yes` metadata matches active portrait classification for every direct `create_country_leader` block in scope.
  - Result: `missing_sprite_defs 0 []`
  - Result: `missing_textures 0 []`
  - Result: `duplicate_custom_leader_hash_groups 0`
- `python3` randomizer pool audit:
  - Result: female assignment pools only for `BAC NLC TSC UDC UWD`.
  - Result: male assignment pools only for `ALA ALN ARD BBH BSC DHC DSC FEV FTH GAC ICD IUL KHC KHW KRS KZR MRC NRF OGB PRA RMC SDZ SOG SZA TNC`.
  - Result: `multi_or_missing_flags {}`.
- `python3` TGA header audit:
  - Result: `checked_flag_files 480`
  - Result: `missing 0`
  - Result: `bad_headers 5`, all five are `gfx/flags/small/SOG*.tga` 8 bpp files.
- `file gfx/flags/small/SOG*.tga`:
  - Result: all five SOG small flags reported as `Targa image data - Map (...) 10 x 7 x 8`.
- `file gfx/flags/small/ALN*.tga` comparison:
  - Result: neighboring ALN small flags report `Targa image data - RGBA 10 x 7 x 32 - 8-bit alpha`.

## Skipped Validation

- No in-game validation was run.
- No image conversion validation was run because the task explicitly forbids generating or altering image files.
- No focus, decision, balance, map, military, or AI validation was run because those surfaces were outside the bounded task.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_country_portrait_name_flag_audit.md`

## Changed Identifiers

- None. No gameplay identifiers, tags, state ids, leader ids, parties, focus tree ids, localisation keys, scripted effects, or formable ids were changed.

## Before And After Behavior

- Before: no gameplay behavior changed by this audit.
- After: no gameplay behavior changed by this audit. Parent now has a bounded evidence handoff confirming leader portrait/name metadata consistency and flag existence, with one remaining SOG small-flag format risk.

## Remaining Setup Or Identity Risks

- Only verified risk in scope: `SOG` small flag files exist but are 8 bpp color-mapped TGAs. If the parent wants strict consistency with the rest of Event 005 flag outputs, route an asset-only re-export for those five small flags.
- Several one-person portrait countries keep institutional initial names in history, then immediately randomize into personal names. This is consistent only because current active portrait classifications read those final DDS files as one-person portraits. If the parent treats any of those portraits as institutional/council portraits, that becomes a hard blocker until the personal randomizer is removed for each affected tag.
