# Event 005 Soviet Collapse Visual Asset Sidecar

Audit date: 2026-05-24

Scope: generated-event-art sidecar for active Event 005 Soviet Collapse leader/council portraits and country flags. This pass is asset and handoff documentation only. It does not edit gameplay, localisation, history, focus, event, interface, or spreadsheet files.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- `common/country_tags/chaosx_countries.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md`

## Active Portrait Audit

Active portrait scope is the Event 005 portrait sprite set registered in:

- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`

Result:

- Active Event 005 portrait sprites checked: `37`
- Missing active portrait DDS files: `0`
- Duplicate active portrait DDS hashes: `0`
- Bad active portrait dimensions: `0`
- Expected portrait size: `156x210`
- Final portrait folder: `gfx/leaders/005_soviet_collapse/`

No new portrait generation was needed. The active `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` council portraits are already covered by `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md` and existing generated-source sidecar copies.

## Active Flag Audit

Active Event 005 custom flag scope:

`ALA`, `ALN`, `ARD`, `BAC`, `BBH`, `BSC`, `CFR`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `MFR`, `MRC`, `NLC`, `NRF`, `OGB`, `PRA`, `RMC`, `SDZ`, `SOG`, `SZA`, `TNC`, `TSC`, `UDC`, `UWD`

Active route/cosmetic flag scope:

- `UKR_BLACK_BANNER`

Result across base, `_communism`, `_democratic`, `_fascism`, and `_neutrality` variants:

- Normal flags checked: `165`, expected size `82x52`, missing `0`, duplicate hashes `0`
- Medium flags checked: `165`, expected size `41x26`, missing `0`, duplicate hashes `0`
- Small flags checked: `165`, expected size `10x7`, missing `0`, duplicate hashes `0`
- Final flag folders: `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`

No new flag generation was needed for active Event 005 custom or route/cosmetic flags.

## Existing-Country Flag Rule

The apparent missing mod-side base flags for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` were not treated as asset gaps. These are vanilla-supported tags, and the existing Event 005 handoff states that ordinary/internal vanilla-supported tags must use game-provided base and ideology flags by default. This pass therefore did not create `gfx/flags/<TAG>.tga` overrides for those countries.

Existing-country flag changes should remain explicit cosmetic-tag route changes. The active example is `UKR_BLACK_BANNER`; no default `UKR` override was created or changed.

## Source Notes

- No `$imagegen` prompt was issued in this pass because the active audit found no missing or non-unique Event 005 portrait/flag assets needing new generated artwork.
- Existing fictional/council portraits and generated/custom flag sources remain documented in `docs/assets/005_soviet_union_collapse/gfx_handoff.md`, `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md`, `docs/assets/005_soviet_union_collapse/base_flag_duplicate_correction/manifest.md`, and `docs/assets/005_soviet_union_collapse/remaining_custom_flag_correction/manifest.md`.
- Historical-restoration flag source notes for `KZR`, `SOG`, `KHW`, `ALN`, and `OGB` remain in `docs/assets/005_soviet_union_collapse/gfx_handoff.md`.

## Out Of Scope

- `ZZZ` flag ideology variants have duplicate hashes in the broad repository flag audit, but `ZZZ` is not an Event 005 Soviet Collapse country or route. This sidecar did not change or regenerate `ZZZ` assets.
- Stale inactive tags such as `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS` were not revived or regenerated.

## Status

Complete for the requested sidecar audit. No new generated visual assets were required.

