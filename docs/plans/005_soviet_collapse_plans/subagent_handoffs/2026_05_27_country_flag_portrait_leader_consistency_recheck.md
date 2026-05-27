# Event 005 Country Flag, Portrait, And Leader Consistency Recheck

Date: 2026-05-27

Scope: bounded Event 005 Soviet Collapse sidecar audit for country flags, leader portraits, leader metadata, and generated leader-name consistency. This is not an Event 005 completion audit.

## Inputs Read

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Portrait modding, Graphical asset modding, Interface modding, Cosmetic tag modding, and Namelist modding.
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `loc_objects_documentation.md`.
- Vanilla precedent: `common/characters/SOV.txt` for portrait-backed character wiring.

## Surfaces Audited

- Event 005 custom/splinter/restoration history files under `history/countries/`
- `common/scripted_effects/005_soviet_collapse_effects.txt` leader-name and event-created council helper blocks
- `interface/005_soviet_collapse*_icons.gfx` portrait sprite mappings
- `gfx/leaders/005_soviet_collapse/*.dds`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` for active Event 005 custom, restoration, and route cosmetic tags
- `docs/assets/005_soviet_union_collapse/manifest.md`
- Existing Event 005 asset and country-package handoffs under this folder

## Findings

Positive findings:

- Active flag scope checked: 32 custom/restoration/splinter tags plus `UKR_BLACK_BANNER`.
- Expected active flag files checked: 495. Missing files: 0.
- All audited normal flags are 82x52, medium flags are 41x26, small flags are 10x7.
- All audited active flag TGAs are 32bpp and use bottom-origin headers; no likely upside-down TGA header was found.
- Exact duplicate flag hash groups inside active same-tag flag families: 0.
- No mod-side default flag overrides were found for vanilla-supported ordinary/internal tags such as `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, or `TAN`. Existing base flags remain vanilla-provided.
- The only existing-country route flag family found in this scope is `UKR_BLACK_BANNER`, which is a focus-applied cosmetic tag route identity rather than a base `UKR` replacement.
- Registered Event 005 portrait sprites checked: 47. All resolve to existing DDS files.
- Referenced Event 005 leader portrait hashes checked: 47. Duplicate hash groups: 0.
- Direct SHA-256 matches against vanilla leader DDS hashes: 0.
- Custom/splinter/restoration history leaders checked: 32. Missing portrait sprites: 0. Missing portrait DDS files: 0.
- `female = yes` metadata and `soviet_collapse_female_single_person_leader_portrait` flags agree in every checked custom history leader.
- The single-person generated leader-name helper has gender-matched branches for the current female-marked tags `BAC`, `NLC`, `TSC`, `UDC`, and `UWD`.
- The male/default generated leader-name helper branches use male-presenting names for the remaining current randomized custom leaders.
- Event-created ordinary/internal council portrait branches are currently wired for `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN`.

Remaining findings and risks:

- Ten Event 005 leader DDS files are present but unreferenced by the currently scanned Event 005 portrait sprite mappings: `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`. They appear stale or reserved; do not count them as active country-package portrait coverage unless they are wired later.
- Generated council portrait sidecar files for `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, and `TAT` remain documentation/package-side assets only unless separately promoted into live `gfx/leaders`, `.gfx`, and scripted leader branches.
- The mechanical flag audit proves size, header orientation, bpp, presence, and exact uniqueness. It cannot fully prove the art-direction rule that every ideology variant is a strong "real design" rather than a simple visual idea. No deterministic duplicate or same-file recolor failure was found.
- Most custom leaders are named as institutional councils in history and then optionally randomized into single-person names by `soviet_collapse_randomize_single_person_leader_name`. That is internally gender-matched, but it remains a design choice: if a portrait is intended to represent an institution rather than one person, the randomization helper should be removed for that tag in a separate design pass.

## Patches

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_27_country_flag_portrait_leader_consistency_recheck.md`

No gameplay, localisation, `.gfx`, history, country, focus, decision, balance, or binary asset files were edited in this recheck.

## Exact Asset Queue If Needed

No generated-art worker queue is required from this audit. The audited active flag and portrait assets are present, correctly sized, not upside-down by TGA header, not vanilla portrait hash matches, and not exact duplicate hashes.

If a later human visual review decides that an ideology flag family is still too simple despite passing the mechanical audit, route it to `chaosx_generated_event_art` with this exact queue format:

1. For each accepted tag family, generate one full 5-flag family: base, `_communism`, `_democratic`, `_fascism`, `_neutrality`.
2. Preserve existing-country base flags. Do not generate `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, or `TAN` base replacements.
3. For route identities, generate only the cosmetic tag family, e.g. `UKR_BLACK_BANNER`, and keep the route wired through `set_cosmetic_tag`.
4. Final outputs must be uncompressed 32bpp bottom-origin TGA files at `82x52`, `41x26`, and `10x7`, placed in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
5. Each ideology variant must be a distinct designed flag with different heraldic composition or emblem logic, not a palette swap, filter pass, or simple geometric recolor of the base.
6. Include source PNGs, processed previews, final TGAs, normal/medium/small contact sheets, TGA header audit, and manifest rows under `docs/assets/005_soviet_union_collapse/`.

## Validation

Ran:

- `python3` TGA header audit over 495 active Event 005 custom/restoration/route flag files.
- `python3` SHA-256 duplicate audit over active same-tag flag families.
- `python3` portrait sprite-to-DDS audit for `interface/005_soviet_collapse*_icons.gfx`.
- `python3` direct SHA-256 comparison between referenced Event 005 leader DDS files and vanilla `gfx/leaders/**/*.dds`.
- `identify gfx/leaders/005_soviet_collapse/*.dds` dimension check; referenced portraits are 156x210.
- `rg` checks for `set_cosmetic_tag`, `UKR_BLACK_BANNER`, generated leader-name helper branches, and mod-side default flag overrides for vanilla-supported tags.
- ImageMagick-backed grayscale/edge scan for closest same-tag normal flag pairs as a rough visual-similarity smoke check.

Skipped:

- No in-game parser or live-session validation.
- No manual image viewing inside this pass; visual distinctiveness conclusions are limited to deterministic file/header/hash checks and prior asset manifests.
- No focus, decision, balance, AI strategy, or map setup validation, per prompt scope.
- No binary asset generation or replacement.

## Completion Statement

This sidecar audit is complete for the requested flags/portraits/leaders consistency surface. Event 005 itself is not complete, and this handoff must not be used as an Event 005 completion claim.
