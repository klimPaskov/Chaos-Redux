# Event 005 Generated Asset Handoff Follow-Up

Audit date: 2026-05-25

Scope: bounded generated-event-art sidecar for Event 005 Soviet Collapse fictional/council portraits and fictional ideology/route flags.

This pass did not edit gameplay, `.gfx`, localisation, focus, decision, event, history, country, spreadsheet, or active asset files. No generated source PNG, processed PNG, contact sheet, DDS, or TGA was created in this follow-up because the current active asset audit found no deterministic missing generated asset and the active flag files are dirty in the worktree.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25/manifest.md`
- `docs/assets/005_soviet_union_collapse/event005_asset_sidecar_2026_05_24.md`
- `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md`
- `docs/assets/005_soviet_union_collapse/visual_asset_sidecar_2026_05_24/manifest.md`

The required offline HOI4 wiki pages and vanilla documentation folder were consulted for repository compliance. This sidecar did not change any Clausewitz script.

## Current Active Result

- Active Event 005 leader/council portrait DDS files checked: `42`.
- Active leader source/processed sidecar coverage: no missing source or processed PNG sidecars for current `gfx/leaders/005_soviet_collapse/*_leader.dds`.
- Scoped active flag families checked: `33` tag/cosmetic families x base plus four ideology suffixes = `165` files in each of normal, medium, and small folders.
- Expected dimensions confirmed by file audit: normal `82x52`, medium `41x26`, small `10x7`.
- Missing scoped active flag files: `0`.
- Duplicate scoped active flag hash groups: `0` in normal, `0` in medium, `0` in small.

## Portraits Still Needing Generation

No active fictional/council/factory/high-chaos portrait needs generation in the current working tree.

Blocked until parent confirmation:

| Tag | Current state | Handoff |
| --- | --- | --- |
| `BEC` | tracked DDS deleted; prior audit found no active references | Generate a fictional council portrait only if the tag is restored to active use. |
| `BLT` | tracked DDS deleted; prior audit found no active references | Generate a fictional council portrait only if the tag is restored to active use. |
| `COU` | tracked DDS deleted; prior audit found no active references | Generate a fictional council portrait only if the tag is restored to active use. |
| `ILU` | tracked DDS deleted; prior audit found no active references | Generate a fictional council portrait only if the tag is restored to active use. |
| `IRA` | tracked DDS deleted; prior audit found no active references | Generate a fictional council portrait only if the tag is restored to active use. |

If any of these are revived, use generated fictional/collective council art only. Do not generate real leader likenesses.

## Flags Still Needing Generation

No active custom/restoration/route flag family has a deterministic missing-file or duplicate-hash generation blocker in this follow-up audit.

Generation or re-export candidates:

| Target | Current state | Handoff |
| --- | --- | --- |
| `UKR_BLACK_BANNER_communism`, `_democratic`, `_fascism`, `_neutrality` | Active TGAs exist in all three sizes and processed previews exist, but standard per-variant source PNGs were not found; earlier source appears to be a combined contact strip. | If source coverage must be clean, crop/re-export distinct source PNGs from the recorded strip or regenerate four distinct fictional route-ideology variants. Preserve `UKR_BLACK_BANNER.tga` unless explicitly scoped. |
| `PRA` base plus ideology variants | Prior handoff marked these as visual-review candidates, not deterministic blockers. | Generate only if the parent accepts active replacement; make one unique base and four unique ideology designs, not recolors/simple-shape variants. |
| `MFR_democratic`, `MFR_fascism`, `MFR_neutrality` | Prior handoff marked these as visual-review candidates, not deterministic blockers. | Generate only if the parent accepts active replacement; keep the base unless explicitly scoped. |
| `BEC`, `BLT`, `COU`, `ILU`, `IRA` flag families | Prior sidecar found these stale/inactive families byte-identical across base and ideology variants. | Generate unique base/ideology flag families only if the tags are restored to active use. |

## Preservation Rules

Base flags for existing vanilla-supported countries should be preserved. Do not create or overwrite default no-suffix base flags for `SOV`, `RUS`, `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, or `FER` from this generated-art route.

Existing-country route changes must remain explicit cosmetic/route tags, such as `UKR_BLACK_BANNER`, rather than default country overrides.

All fictional ideology and route flags must be intentional unique generated/source designs. Do not satisfy ideology variants by applying a color filter, flipping a flag, adding one basic shape, copying one emblem onto the base, or making byte-identical variants.

## Blockers and Uncertainty

- The active flag files are dirty in the worktree, so this sidecar did not overwrite any `gfx/flags/**` file.
- Visual quality candidates such as `PRA` and `MFR` are design calls, not deterministic blockers from this audit.
- No contact sheet was created in this follow-up because the existing `generated_asset_handoff_2026_05_25` contact sheets already cover the current active portrait and flag surface, and no new image outputs were produced.
