# Event 005 Leader and Flag Gap Handoff - 2026-05-26

Scope: read-only inventory plus handoff for Event 005 Soviet Collapse new-leader/council portraits and flags. No gameplay, localisation, `.gfx`, focus, event, decision, trigger, spreadsheet, live portrait, or live flag files were edited.

## Created files

- `docs/assets/005_soviet_union_collapse/leader_flag_gap_handoff_2026_05_26.md`

No source PNG, processed PNG, DDS, or TGA assets were created. The active portrait and flag surface is already covered, and several live flag/interface files are dirty from prior work.

## Current dirty asset state

Scoped worktree inspection found existing dirty files in the Event 005 asset surface before this handoff update:

- Modified docs: `docs/assets/005_soviet_union_collapse/gfx_handoff.md`, `docs/assets/005_soviet_union_collapse/manifest.md`.
- Modified normal flag files for `ALN`, `CFR`, `KHW`, `KRS`, `KZR`, `RMC`, `SDZ`, `SOG`, `TSC`, and `UDC`, with ideology variants dirty for `ALN`, `KHW`, `KZR`, and `SOG`.
- Modified medium flag files for the same normal-flag group, with ideology variants dirty for `ALN`, `KHW`, `KZR`, and `SOG`.
- Modified small flag files for `ALN`, `CFR`, `KHW`, `KRS`, `KZR`, `RMC`, `SDZ`, `SOG`, `TSC`, and `UDC`, with `_communism`, `_democratic`, `_fascism`, and `_neutrality` dirty for every listed tag.
- No dirty files were found under `gfx/leaders/005_soviet_collapse/` during the scoped status check.

This sidecar does not restore, overwrite, or promote any of those dirty flag assets. Preserve existing no-suffix base flags unless the parent explicitly scopes a new Event 005 country base flag or an existing-country cosmetic tag.

## References inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Offline wiki core pages required by `AGENTS.md`, plus country creation, national focus, and cosmetic tag pages.
- Vanilla docs: `common/characters/_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`.
- Asset references: `.agents/skills/chaos-redux-event-assets/assets/flags/`, `gfx/leaders/005_soviet_collapse/`, and existing Event 005 `docs/assets` manifests/handoffs.
- Read-only script surfaces: `common/country_tags/chaosx_countries.txt`, Event 005 `history/countries/*`, Event 005 focus/decision/event files, and Event 005 `.gfx` portrait references.

## Active custom-country inventory

Active Event 005 custom tags from `common/country_tags/chaosx_countries.txt`: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`.

Portrait audit result: all 32 active tags have a `create_country_leader` picture in `history/countries/`, a matching sprite in Event 005 `.gfx`, a final `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`, a source PNG, and a processed PNG. No active council portrait gap was found.

Flag audit result: all 32 active tags have normal, medium, and small TGA files for base plus `_communism`, `_democratic`, `_fascism`, and `_neutrality`. Dimensions are correct: normal `82x52`, medium `41x26`, small `10x7`. All checked TGA files are 32-bit with descriptor byte `0x08`. Exact duplicate audit found zero duplicate groups and zero same-tag exact duplicate variants.

Orientation confirmation: the active custom-country flag audit checks the vanilla-compatible bottom-origin convention by descriptor byte. Normal, medium, and small outputs are all 32-bit TGA files with descriptor `0x08`; the expected dimensions are normal `82x52`, medium `41x26`, and small `10x7`.

## Existing-country and route/cosmetic notes

- `FER`, `MOL`, `UZB`, `TAJ`, `TMS`, and `KYR` are referenced by Event 005 focus/decision logic but are not Event 005 custom tags in `chaosx_countries.txt`. Preserve their existing/vanilla base flags. Do not create no-suffix base flags for them from this sidecar.
- Event 005 already has portrait sprites and DDS files for `FER`, `MOL`, `UZB`, `TAJ`, and `TMS` under `gfx/leaders/005_soviet_collapse/`, but there is no matching custom-tag history leader definition in this inventory. Main agent should decide whether those are intentionally wired for vanilla/released republic leadership before requesting more art.
- `KYR` is referenced in the central Asia focus/decision route but has no Event 005 custom portrait target in the inspected sidecar manifests. Treat a Kyrgyz council portrait as blocked pending main-agent design and wiring scope.
- `UKR_BLACK_BANNER` is an explicit cosmetic tag in `common/countries/cosmetic.txt`, not a default `UKR` base flag replacement. Existing target paths are `gfx/flags/UKR_BLACK_BANNER[_ideology].tga`, `gfx/flags/medium/UKR_BLACK_BANNER[_ideology].tga`, and `gfx/flags/small/UKR_BLACK_BANNER[_ideology].tga`.

## Recommended target paths

For active custom-country portraits, keep the existing target pattern:

- Final DDS: `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`
- Source PNG: `docs/assets/005_soviet_union_collapse/source_png/<TAG>_leader_source.png`
- Processed PNG: `docs/assets/005_soviet_union_collapse/processed_png/<TAG>_leader.png`
- Sprite owner: existing Event 005 `.gfx` file that already defines the `GFX_portrait_<TAG>_*` sprite.

For active custom-country flags, keep:

- Normal: `gfx/flags/<TAG>[_ideology].tga`
- Medium: `gfx/flags/medium/<TAG>[_ideology].tga`
- Small: `gfx/flags/small/<TAG>[_ideology].tga`

For existing-country route flags, use explicit cosmetic-tag filenames only. Do not create or replace `UKR.tga`, `MOL.tga`, `UZB.tga`, `TAJ.tga`, `TMS.tga`, `KYR.tga`, or `FER.tga` unless the parent explicitly scopes a sourced historical/cosmetic replacement.

## Flag source-mode recommendations

- Fictional/generated mode: invented Event 005 custom tags such as `CFR`, `MFR`, `SDZ`, `TSC`, `UDC`, `RMC`, `DSC`, `NRF`, and other high-chaos councils, when the design is clearly fictional.
- Source-research mode: `OGB`, `KZR`, `SOG`, `KHW`, and `ALN` if the requested design uses historically attested symbols, medieval motifs, tamgas, seals, scripts, heraldry, or restoration claims.
- Existing-country mode: `UKR`, `MOL`, `UZB`, `TAJ`, `TMS`, `KYR`, and `FER` base flags should be preserved; any route-specific variants need explicit cosmetic tags and main-agent wiring.

## Blocked gaps

- No active Event 005 custom-country portrait or flag file is blocked by missing art.
- `KYR` council portrait and any `KYR` route flag are blocked pending main-agent decision because the inspected docs/manifests do not define an exact target asset, sprite name, or source mode.
- Inactive/stale asset families such as `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS` should not receive new generated portraits or flags unless the main agent restores those tags to active country-package use.

Exact remaining generated-fictional asset gaps from this audit:

- Active Event 005 custom country tags: none.
- Active `UKR_BLACK_BANNER` cosmetic route flag package: none; base plus four ideology variants exist in normal, medium, and small sizes with correct TGA header convention and no exact same-tag duplicate variants.
- Existing/vanilla country tags: no default base-flag work should be generated from this sidecar. Any future `KYR`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, or similar route flag needs an explicit cosmetic tag and parent wiring scope first.

## Main-agent wiring later

- No `.gfx` edit is required for the 32 active custom-country portraits found in this audit.
- If the main agent promotes existing sidecar-only assets, compare them against the dirty live files first and wire only the selected final assets.
- If adding `KYR` or existing-republic council leadership, first define whether it replaces a vanilla leader, uses a fictional council/cosmetic route, or needs a real-person sourced portrait. Then request a bounded portrait asset with exact sprite name and final DDS path.
- Re-run flag contact sheets after any promoted flag change: normal, medium, small orientation; TGA descriptor/header convention; exact duplicate groups; same-tag uniqueness; and visual readability at `82x52`, `41x26`, and `10x7`.
