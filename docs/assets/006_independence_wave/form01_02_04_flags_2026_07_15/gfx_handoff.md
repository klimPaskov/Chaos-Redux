# Event 006 FORM-01, FORM-02, and FORM-04 flag handoff

These are shared alternate-history base flags. Their ideology-suffixed files
are exact byte copies of the approved base design, not visually distinct
ideology variants, route variants, historical reconstructions, or
cosmetic-route recolours.

HOI4 country flags are filename-resolved and require no `.gfx` sprite
definition. No `.gfx`, GUI, gameplay, country-tag, or localisation file was
edited by this asset package.

| Identity | Tag | Normal | Medium | Small |
| --- | --- | --- | --- | --- |
| Celtic Congress | `KCX` | `gfx/flags/KCX.tga` | `gfx/flags/medium/KCX.tga` | `gfx/flags/small/KCX.tga` |
| North Atlantic Union | `NUX` | `gfx/flags/NUX.tga` | `gfx/flags/medium/NUX.tga` | `gfx/flags/small/NUX.tga` |
| Rhenish League | `RLX` | `gfx/flags/RLX.tga` | `gfx/flags/medium/RLX.tga` | `gfx/flags/small/RLX.tga` |

Each tag also has explicit `_democratic`, `_communism`, `_fascism`, and
`_neutrality` filenames at all three sizes. Every alias is byte-identical to
the corresponding base file shown above, preserving the accepted shared-design
rule while covering HOI4's ideology filename resolution.

All nine files are uncompressed 32-bit RGBA TGAs with bottom-left origin. The
Git `file.exe` utility reports each as `Targa image data - RGBA ... - 8-bit
alpha` and none reports the `- top` origin suffix.

The accepted research supports one shared design per tag. Do not replace the
ideology aliases with recolours, altered emblems, route designs, or separate
cosmetic designs. The parent implementation owns tag registration and identity
adapter calls and must preserve this one-design rule.

Package review files:

- `contact_sheets/source_masters_contact_sheet.png`
- `contact_sheets/source_vs_final_contact_sheet.png`
- `contact_sheets/final_size_ladder_native_contact_sheet.png`
- `contact_sheets/final_size_ladder_enlarged_nearest_contact_sheet.png`
- `metadata/flag_validation.json`
- `metadata/checksums.sha256`
