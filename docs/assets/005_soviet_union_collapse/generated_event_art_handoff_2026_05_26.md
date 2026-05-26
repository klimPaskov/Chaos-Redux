# Event 005 Generated Portrait and Flag Handoff, 2026-05-26

Scope: bounded generated-event-art sidecar for Event 005 Soviet Union Collapse fictional/council portraits and fictional/custom ideology flags. This pass is documentation-only. It did not edit gameplay, localisation, `.gfx`, script, history, focus, decision, country, or spreadsheet files, and it did not overwrite existing portrait or flag assets.

## References inspected

- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/portrait_sidecar_2026_05_24.md`
- `docs/assets/005_soviet_union_collapse/generated_portrait_audit_2026_05_25/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25/gfx_handoff.md`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`
- `.agents/skills/chaos-redux-event-assets/assets/flags`
- Read-only sprite reference check in `interface/005_soviet_collapse_custom_icons.gfx` and `interface/005_soviet_collapse_factory_ancient_icons.gfx`

## Current active portrait state

Active referenced fictional/council portrait sprites: `37`.

All `37` active references point to existing `156x210` DDS files under `gfx/leaders/005_soviet_collapse/`.

Active referenced tags:

`ALA`, `ALN`, `ARD`, `BAC`, `BBH`, `BSC`, `CFR`, `DHC`, `DSC`, `FER`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `MFR`, `MOL`, `MRC`, `NLC`, `NRF`, `OGB`, `PRA`, `RMC`, `SDZ`, `SOG`, `SZA`, `TAJ`, `TMS`, `TNC`, `TSC`, `UDC`, `UWD`, `UZB`.

Final DDS pattern:

- `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`

Sprite handoff:

- Keep existing `GFX_portrait_*` sprite names in `interface/005_soviet_collapse_custom_icons.gfx` and `interface/005_soviet_collapse_factory_ancient_icons.gfx`.
- No new portrait sprite name is proposed by this sidecar.
- No `.gfx` edit is required for the current active portrait set.

Inactive or stale portrait files still present in the final folder:

`BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, `TRS`.

These were not changed. Do not regenerate, delete, or wire them from the generated-art sidecar unless the parent explicitly confirms that the tags are active Event 005 content again.

## Current flag state

Complete custom flag families found with base plus `communism`, `democratic`, `fascism`, and `neutrality` variants in normal, medium, and small folders: `42`.

Complete custom/cosmetic flag families:

`ALA`, `ALN`, `ARD`, `BAC`, `BBH`, `BEC`, `BLT`, `BSC`, `CFR`, `COU`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `ILU`, `IRA`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `LID`, `MFR`, `MRC`, `NLC`, `NRF`, `OGB`, `PRA`, `RCD`, `RLD`, `RMC`, `SDZ`, `SEP`, `SOG`, `SZA`, `TNC`, `TRS`, `TSC`, `UDC`, `UWD`.

Final flag patterns:

- Normal: `gfx/flags/<TAG>[_<ideology>].tga`, `82x52`
- Medium: `gfx/flags/medium/<TAG>[_<ideology>].tga`, `41x26`
- Small: `gfx/flags/small/<TAG>[_<ideology>].tga`, `10x7`

Flag handoff:

- HOI4 country flags do not need `.gfx` sprite entries.
- No new base no-suffix flags should be created for vanilla-supported ordinary/internal tags.
- Existing-country route flag changes must use explicit cosmetic tags. The current documented example remains `UKR_BLACK_BANNER`.
- `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` have active generated council portraits, but no custom default flag family should be created for those vanilla-supported tags.

## Assets completed by prior passes

- Active generated/council portrait coverage is already present for the `37` active referenced portrait sprites.
- Active custom/cosmetic flag families are already present in normal, medium, and small sizes for the custom tags listed above.
- Existing Event 005 documentation records generated/source PNGs, processed previews, final portrait DDS files, final flag TGA files, and contact sheets in the earlier sidecar packages.

## Assets still needed

None found in this bounded generated-art audit for the current active portrait and custom/cosmetic flag surfaces.

Do not create any of the following without a parent confirmation that the tag or route is active and intentionally in scope:

- New default flags for vanilla-supported tags: `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`.
- New/generated replacements for inactive or stale portrait tags: `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, `TRS`.
- New base flag redesigns for existing active custom tags unless the parent explicitly requests a base-flag replacement. Ideology variants must remain distinct designs, not recolors, filters, flips, copied emblems, or simple shape additions.

## Blockers and uncertainty

- No image generation was performed because no active missing generated portrait or custom/cosmetic flag gap was found.
- The working tree already has unrelated dirty Event 005 asset/docs changes, including `docs/assets/005_soviet_union_collapse/manifest.md`, `docs/assets/005_soviet_union_collapse/gfx_handoff.md`, and scoped flag TGA files. This sidecar does not interpret or revert those changes.
- Repository flag files outside Event 005 scope, such as `ZZZ`, `mengele_*`, and `germany_mengele_*`, have separate format issues in a broad TGA scan; they are not part of this Event 005 handoff.
