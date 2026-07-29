# Event 012 Africa achievement icon handoff

## Handoff status

The 44 normal, 44 grey, and 44 not-eligible processed PNGs are converted into the 132 runtime DDS files.

No `.gfx` edit is required for the custom achievement IDs under the current project convention because the achievement UI resolves root files by exact achievement ID.

The parent agent owns final gameplay/UI review and any interface registration required by the live implementation.

## Runtime naming contract

For every key listed in `manifest.md`, place three 64x64 DDS files directly under `gfx/achievements/`:

```text
gfx/achievements/<key>.dds
gfx/achievements/<key>_grey.dds
gfx/achievements/<key>_not_eligible.dds
```

The normal, grey, and not-eligible states must be purpose-built variants of the matching key and must not reuse a focus, idea, decision, host-overlay, or member-package icon.

The expected path is root-only `gfx/achievements/`, not an event subfolder.

## Evidence inputs

Use `processed_png/<key>.png`, `processed_png/<key>_grey.png`, and `processed_png/<key>_not_eligible.png` as the 64x64 sources for each state.

Use `validation/asset_validation.tsv` and `validation/hashes.sha256` to confirm source and processed bytes before conversion.

Use `contact_sheets/africa_achievement_processed_contact_sheet.png` for the visual review pass.

All 132 final runtime DDS triplets are present under `gfx/achievements/`.

`validation/dds_validation.tsv` records exact 64x64 dimensions, headers, hashes, and pixel equality for every triplet member.
