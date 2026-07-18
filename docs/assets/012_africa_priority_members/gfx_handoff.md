# Event 012 Priority Member GFX Handoff

## Runtime registration

The stable decision sprite registrations live in `interface/012_africa_priority_member_assets.gfx`. This tranche did not rename or duplicate any sprite. Its 40 final files were written directly to the registered folder:

`gfx/interface/decisions/012_africa/priority_members/`

Present files cover:

- eight shared priority-member decision surfaces;
- sixteen package-specific distinct-mechanic decisions;
- sixteen package-specific national-force decisions.

The sixteen package-specific post-settlement decision sprites are registered in the same GFX file but still have no final DDS. No fallback texture is assigned.

## Final-file contract

- Canvas: 32x32.
- Alpha: retained.
- DDS: uncompressed 32-bit BGRA.
- Runtime file name: identical to the processed PNG stem with `.dds` extension.
- Sprite name: identical to the runtime file stem with the `GFX_` prefix.

The processed PNG and final DDS inventories are one-to-one: 40 processed PNGs and 40 final DDS files.

## Review surfaces

Source-scale and gameplay-scale contact sheets are retained in `contact_sheets/`:

- `012_africa_priority_member_shared_contact_sheet.png`
- `012_africa_priority_member_forces_contact_sheet.png`
- `012_africa_priority_member_mechanics_contact_sheet.png`
- `012_africa_priority_member_shared_runtime32_contact_sheet.png`
- `012_africa_priority_member_forces_runtime32_contact_sheet.png`
- `012_africa_priority_member_mechanics_runtime32_contact_sheet.png`

The source-scale sheets show the original opaque magenta production matte. The runtime sheets composite the processed 32x32 alpha assets over neutral grey for edge and legibility review.

## Remaining wiring blockers

The following registrations still point to absent files:

- 16 post-settlement decision DDS files;
- 8 focus DDS files;
- 35 idea DDS files;
- 4 report-event DDS files;
- 16 institutional-council portrait DDS files.

The sixteen cosmetic country identities now have country-colour definitions, but still require 48 three-size flag files. Those files are outside this 40-icon conversion tranche and remain explicit package blockers.
