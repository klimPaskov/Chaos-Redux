# Event 005 Visual Asset Sidecar Validation

Validation date: 2026-05-24

## Commands Run

- Read required repo and skill guidance: `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and official `imagegen` skill guidance.
- Inspected relevant offline Paradox wiki pages and vanilla documentation enough to confirm this pass stayed asset-only.
- Audited active portrait references from `interface/005_soviet_collapse_custom_icons.gfx` and `interface/005_soviet_collapse_factory_ancient_icons.gfx`.
- Audited active custom/cosmetic flag files in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Used `identify` for active image dimension checks and SHA-256 hashes for duplicate detection.

## Portrait Validation

- Active Event 005 portrait sprites: `37`
- Missing DDS files: `0`
- Duplicate active portrait hashes: `0`
- Bad dimensions: `0`
- Required size: `156x210`

## Flag Validation

Scoped active flags: `32` Event 005 custom tags plus `UKR_BLACK_BANNER`.

Each scoped tag was checked for base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`.

| Folder | Files checked | Expected size | Missing | Duplicate hash groups |
| --- | ---: | --- | ---: | ---: |
| `gfx/flags/` | `165` | `82x52` | `0` | `0` |
| `gfx/flags/medium/` | `165` | `41x26` | `0` | `0` |
| `gfx/flags/small/` | `165` | `10x7` | `0` | `0` |

## Generation Decision

No image generation was run. The active asset audit found no missing or non-unique Event 005 portrait/flag assets in the requested scope.

## Blockers And Uncertainty

- Blockers: none for this sidecar.
- Out-of-scope finding: `ZZZ` ideology flags have duplicate hashes in the broad repository flag audit, but `ZZZ` is not part of Event 005 Soviet Collapse.
- Working tree note: the repository already contains broad unrelated Event 005 and asset changes. This sidecar only adds files under `docs/assets/005_soviet_union_collapse/visual_asset_sidecar_2026_05_24/`.

