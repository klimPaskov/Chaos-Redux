# Event 012 Africa Cosmetic Flags GFX Handoff

No `.gfx` wiring is required for this package.

Country and cosmetic flags resolve by filename in the standard HOI4 flag folders:

- `gfx/flags/`
- `gfx/flags/medium/`
- `gfx/flags/small/`

Root DDS files were still generated and copied into `gfx/flags/` for the completed stems to match the existing Event 012 flag package pattern.

Relevant package DDS records:

- `dds/AFR.dds`
- `dds/AFR_FEDERAL_CHARTER.dds`
- `dds/AFR_SOVEREIGN_SEATS.dds`
- `dds/AFR_PEOPLES_LIBERATION.dds`
- `dds/AFR_CONTINENTAL_COMMAND.dds`
- `dds/AFR_CROWN_CONGRESS.dds`
- `dds/AFR_PAN_ATLANTIC.dds`
- `dds/AFR_ARCHIVE_MANDATE.dds`
- `dds/AFR_WORLD_ROOT.dds`
- `dds/AFR_AFRICAN_MIDDLE_EASTERN_UNION.dds`
- `dds/AFR_AFRO_ASIAN_UNION.dds`
- `dds/AFR_AFRO_EURASIAN_UNION.dds`
- `dds/AFR_AFRO_ATLANTIC_UNION.dds`
- `dds/AFR_CONGRESS_OF_CONTINENTS.dds`

Implementation use note:

- Shared ideology visuals are intentional for all fourteen cosmetic identities in this completion pass.
- Every shared ideology visual was copied to a real ideology filename so no flag fallback behavior is required.
