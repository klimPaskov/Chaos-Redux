# Event 005 Flag and Portrait Sidecar Handoff - 2026-05-26

Scope: generated-event-art sidecar audit for Event 005 Soviet Collapse flags and fictional leader/council portraits. This pass focused only on the user's flag and portrait requirements: preserve base flags for existing countries, do not create new base flags for existing countries, and treat Event 005 flag changes as ideology or cosmetic-route variants only.

No gameplay, localisation, `.gfx`, focus, decision, script, history, country, GUI, spreadsheet, live flag, or live portrait files were edited. No new image generation was performed because the current active generated-art surface has no missing or obviously broken active flag or portrait asset.

## References Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- Required offline wiki core pages under `paradox_wiki/`, including the singular `Effect - Hearts of Iron 4 Wiki.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_union_collapse/event005_asset_sidecar_2026_05_24.md`
- `docs/assets/005_soviet_union_collapse/visual_asset_sidecar_2026_05_24/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_event_art_handoff_2026_05_26.md`
- `docs/assets/005_soviet_union_collapse/leader_flag_gap_handoff_2026_05_26.md`
- `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_small_flag_export_fix/manifest.md`
- `docs/assets/005_soviet_collapse/generated_event_art_first_batch_2026_05_25/manifest.md`
- `docs/assets/005_soviet_collapse/generated_country_visual_sidecar_2026_05_25/manifest.md`
- Read-only checks of `interface/005_soviet_collapse_custom_icons.gfx`, `interface/005_soviet_collapse_factory_ancient_icons.gfx`, `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`, and `gfx/leaders/005_soviet_collapse/`

## Worktree Safety

The worktree was already dirty before this handoff. The scoped dirty asset surface includes the known problem flag families `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR`, plus `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` leader DDS files. This pass did not overwrite those live files.

Because active flag and portrait files are already dirty, any future replacement should compare the selected source sidecar against current live files before promotion.

## Existing-Country Flag Rule

No default base flag should be generated for vanilla-supported or existing country tags from this sidecar. The preserved existing-country set remains:

`UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.

The read-only path audit found no mod-side default flag overrides for those tags under `gfx/flags/`, `gfx/flags/medium/`, or `gfx/flags/small/`.

Route-specific existing-country flag changes should use explicit cosmetic tags only. The current documented example remains `UKR_BLACK_BANNER`; this audit did not change it.

## Scoped Flag Audit

Known problem families checked directly: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR`.

For each family, base plus `_communism`, `_democratic`, `_fascism`, and `_neutrality` variants exist in:

- `gfx/flags/` at `82x52`
- `gfx/flags/medium/` at `41x26`
- `gfx/flags/small/` at `10x7`

Direct TGA header reads found all checked files are type `0x02`, `32` bpp, descriptor byte `0x08`. Exact same-tag duplicate checks found `5/5` unique hashes for each family at each size, so no checked family is byte-identical across base and ideology variants.

### Flags Still Needing Regeneration Or Flipping

None in the active scoped generated-art surface.

The earlier `generated_event_art_first_batch_2026_05_25` report's small-flag problem list is superseded by the later small-flag export fix and the direct header check in this pass. The stale `current_live_asset_surface.tsv` rows that show `descriptor_byte = 0x00` for the same small flags are not current for the live files inspected in this pass.

If visual-quality replacement is later requested:

- `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, and `UDC` can be routed as fictional/generated ideology variant work.
- `SOG`, `ALN`, `KHW`, and `KZR` should stay in source-research/historically grounded handling if the design uses restoration symbols, tamgas, seals, medieval motifs, or attested historical claims.
- No existing-country base flag should be created as a shortcut; use a cosmetic tag with explicit main-agent wiring.

## Scoped Portrait Audit

Active referenced Event 005 portrait DDS files in `interface/005_soviet_collapse_custom_icons.gfx` and `interface/005_soviet_collapse_factory_ancient_icons.gfx`: `37/37` present.

All leader/council DDS files currently present under `gfx/leaders/005_soviet_collapse/` identify as `156x210`. A folder-wide SHA-256 duplicate scan found no duplicate leader DDS hashes.

Active referenced tags checked:

`ALA`, `ALN`, `ARD`, `BAC`, `BBH`, `BSC`, `CFR`, `DHC`, `DSC`, `FER`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KHW`, `KRS`, `KZR`, `MFR`, `MOL`, `MRC`, `NLC`, `NRF`, `OGB`, `PRA`, `RMC`, `SDZ`, `SOG`, `SZA`, `TAJ`, `TMS`, `TNC`, `TSC`, `UDC`, `UWD`, and `UZB`.

### Portraits Still Missing Or Duplicated

None in the active referenced Event 005 portrait surface.

Inactive or stale portrait DDS files are still present for `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`. They are not referenced by the active Event 005 portrait `.gfx` files inspected here, so this sidecar did not regenerate, delete, or rewire them.

The older reports that mention missing/deleted `BEC`, `BLT`, `COU`, `ILU`, or `IRA` portraits are superseded for the current working tree: those DDS files are present at `156x210`. The older duplicate release-council pairs (`MOL`/`BEC`, `UZB`/`BLT`, `TAJ`/`COU`, `TMS`/`ILU`, `FER`/`IRA`) are also not present in the current folder-wide SHA-256 scan.

## Generation Decision

No `$imagegen` calls were made.

Generation was not needed for the active scoped assets, and generating replacements would be unsafe in this dirty worktree without a parent-selected exact target, because the live flag and several leader files are already modified by other work.

## Follow-Up For Main Agent

- Treat active scoped flag regeneration/flipping as complete unless visual review rejects a specific design.
- Treat active referenced fictional/council portrait coverage as complete unless a specific portrait is rejected on visual quality.
- Do not request generated base flags for existing countries. Route any existing-country flag change through an explicit cosmetic tag and main-agent wiring.
- Do not revive `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, or `TRS` portraits or flags unless those tags are restored to active Event 005 country-package use.
