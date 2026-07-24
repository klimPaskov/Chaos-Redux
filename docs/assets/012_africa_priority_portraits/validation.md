# Event 012 dramatic portrait validation

- Built-in ImageGen produced 16 unique source masters. The parent visually reviewed the masters and approved the period-grounded council direction, including the Asante, Great Zimbabwe, Merina, and Zulu additions.
- Every current source master and canonical `source_png` copy is a real generated PNG, not a contact sheet or tint pass.
- Repository leader processor produced 16 opaque `156x210` PNGs from the generated masters. Native output alpha extrema are `(255, 255)` for all 16.
- Repository DDS converter produced 16 runtime textures at the exact registered paths. `metadata/dds_validation.json` verifies `DDS ` magic, 124-byte header, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, exact `128 + 156*210*4` length, dimensions, alpha range, and decoded PNG output for every DDS.
- `comparison/processed_contact_sheet_dramatic.png`, `comparison/dds_contact_sheet_dramatic.png`, and `comparison/dramatic_source_processed_dds_contact_sheet.png` show current source/processed/decoded-DDS parity. Parent reviewed the processed and DDS sheets and a native-size Buganda sample; the council faces and phenomena remain readable at runtime size.
- `interface/012_africa_priority_member_characters.gfx` was inspected read-only; all 16 sprite names and texture paths match the runtime DDS filenames. No `.gfx`, gameplay, localisation, or GUI file was edited in this subtask.
- Source research license/attribution remains represented by the retained 16 Wikimedia Commons source originals and source-research package. Generated final assets are marked ImageGen source mode and do not claim a real-person likeness.

Earlier source-photo atmosphere outputs were rejected/superseded and must not be staged as current runtime evidence.
