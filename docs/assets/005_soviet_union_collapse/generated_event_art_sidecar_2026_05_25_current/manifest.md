# Event 005 Generated Event Art Sidecar Manifest

Audit date: 2026-05-25

Scope: bounded generated-art sidecar for Event 005 Soviet Collapse fictional leader/council portraits and fictional custom-country or route flags. This pass did not edit gameplay, localisation, interface `.gfx`, GUI, focus, decision, event, history, country, spreadsheet, or active `gfx/flags/**` / `gfx/leaders/**` files.

## References inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- `gfx/leaders/005_soviet_collapse/`
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`
- `common/country_tags/chaosx_countries.txt`
- `history/countries/* - *.txt` Event 005 custom-country leader references
- `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/manifest.md`
- `docs/assets/005_soviet_union_collapse/generated_asset_handoff_2026_05_25_followup/generated_asset_handoff.md`
- Offline HOI4 wiki core pages required by `AGENTS.md`

The official `$imagegen` skill is available and was read. No image generation call was made in this follow-up because the active package audit found no deterministic missing generated leader/council portrait or custom flag asset, and many active Event 005 flag files are already dirty in the worktree from other work.

## Active package audit

- Event 005 custom/high-chaos country tags checked from `common/country_tags/chaosx_countries.txt`: `32`.
- Active fictional/council leader portrait DDS files expected: `32`.
- Missing active leader DDS files: `0`.
- Active leader source PNG sidecars expected in `docs/assets/005_soviet_union_collapse/source_png/`: `32`.
- Missing active leader source PNG sidecars: `0`.
- Active leader processed PNG previews expected in `docs/assets/005_soviet_union_collapse/processed_png/`: `32`.
- Missing active leader processed PNG previews: `0`.
- Flag families checked: `32` custom tags x base plus four ideology suffixes.
- Missing normal flag files in `gfx/flags/`: `0`.
- Missing medium flag files in `gfx/flags/medium/`: `0`.
- Missing small flag files in `gfx/flags/small/`: `0`.
- Dimension audit: normal flags are `82x52`, medium flags are `41x26`, and small flags are `10x7`.
- Exact file duplicate audit for scoped active flags: `0` duplicate groups in normal, medium, and small folders.

## Assets created or modified

| File | Type | Status |
| --- | --- | --- |
| `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_current/manifest.md` | sidecar manifest | created |
| `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_25_current/gfx_handoff.md` | handoff note | created |

No source PNG, processed PNG, DDS, or TGA output was created in this pass because the existing active Event 005 country package already has complete generated-art coverage for the scoped leaders/councils/flags.

## Deliberately not touched

- No base flags for existing in-game countries were replaced or generated. This includes `SOV`, `RUS`, `UKR`, `BLR`, `KAZ`, `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`.
- No route or ideology flags were overwritten while the active `gfx/flags/**` files are dirty in the worktree.
- No active `gfx/leaders/005_soviet_collapse/*_leader.dds` portrait was overwritten; all scoped active custom-country leaders already have final DDS, source PNG, and processed PNG coverage.
- No Event 005 news, report, or super-event image was generated because this task was bounded to new leaders/councils/flags clearly needed by existing Event 005 country package files.
- No inactive or stale tag families were revived. Prior notes mentioning inactive/deleted `BEC`, `BLT`, `COU`, `ILU`, or `IRA` assets remain blocked unless a parent task restores those tags to active country-package use.

## Blockers and uncertainty

- Several active Event 005 flag files are dirty before this pass. Refining them in place would risk overwriting another worker's edits, so this sidecar only records the audit result.
- Visual quality review of flag designs remains a design judgment. This audit proves presence, dimensions, source-sidecar coverage for active leaders, and absence of exact duplicate flag files; it does not claim every flag is historically ideal or visually final beyond the existing package handoff.

## Status

`complete` for this bounded sidecar audit. No generated final asset was missing from the scoped active Event 005 leader/council/flag surface.
