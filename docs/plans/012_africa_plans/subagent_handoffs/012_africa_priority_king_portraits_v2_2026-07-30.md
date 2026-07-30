# Event 012 Africa priority king portraits v2 handoff

Scope: replacement and visual audit of the 16 fictional high-chaos priority-member sovereign portraits requested for Event 012 Africa. The runtime filenames, dimensions, alpha behavior, sprite ids, and parent-owned country mappings were preserved exactly. No `.gfx`, character, gameplay, localisation, event, focus, decision, or spreadsheet file was edited.

Source and evidence paths are ignored by the repository's `docs/assets/` rule but are present in the workspace:

- Generated masters: `docs/assets/012_africa_priority_portraits/source_generated/portrait_012_africa_priority_<key>_sovereign_source_gen.png` for `asante`, `oyo`, `sokoto`, `kanem_bornu`, `manden`, `kongo`, `buganda`, `aksum`, `harar`, `kilwa`, `nubia`, `luba`, `lunda`, `great_zimbabwe`, `merina`, and `zulu`.
- Byte-for-byte source copies: `docs/assets/012_africa_priority_portraits/source_png/portrait_012_africa_priority_<key>_sovereign_source.png` for the same 16 keys.
- Processed previews: `docs/assets/012_africa_priority_portraits/processed_png/portrait_012_africa_priority_<key>_sovereign.png`, opaque `156x210` PNG for each key.
- Decoded DDS evidence: `docs/assets/012_africa_priority_portraits/comparison/dds_decoded/portrait_012_africa_priority_<key>_sovereign.png` for each key.

Final runtime DDS files under `gfx/leaders/012_africa/priority_members/`:

- `portrait_012_africa_priority_asante_sovereign.dds`
- `portrait_012_africa_priority_oyo_sovereign.dds`
- `portrait_012_africa_priority_sokoto_sovereign.dds`
- `portrait_012_africa_priority_kanem_bornu_sovereign.dds`
- `portrait_012_africa_priority_manden_sovereign.dds`
- `portrait_012_africa_priority_kongo_sovereign.dds`
- `portrait_012_africa_priority_buganda_sovereign.dds`
- `portrait_012_africa_priority_aksum_sovereign.dds`
- `portrait_012_africa_priority_harar_sovereign.dds`
- `portrait_012_africa_priority_kilwa_sovereign.dds`
- `portrait_012_africa_priority_nubia_sovereign.dds`
- `portrait_012_africa_priority_luba_sovereign.dds`
- `portrait_012_africa_priority_lunda_sovereign.dds`
- `portrait_012_africa_priority_great_zimbabwe_sovereign.dds`
- `portrait_012_africa_priority_merina_sovereign.dds`
- `portrait_012_africa_priority_zulu_sovereign.dds`

Visual review evidence:

- `docs/assets/012_africa_priority_portraits/comparison/sovereign_v2_source_contact_sheet.png`
- `docs/assets/012_africa_priority_portraits/comparison/sovereign_v2_source_processed_dds_contact_sheet.png`
- `docs/assets/012_africa_priority_portraits/comparison/sovereign_v2_processed_runtime4x_contact_sheet.png`
- `docs/assets/012_africa_priority_portraits/prompts/sovereign_prompt_records.md`
- `docs/assets/012_africa_priority_portraits/metadata/sovereign_provenance.json`
- `docs/assets/012_africa_priority_portraits/metadata/sovereign_v2_processing.json`
- `docs/assets/012_africa_priority_portraits/metadata/sovereign_v2_dds_validation.json`
- `docs/assets/012_africa_priority_portraits/metadata/sovereign_package_audit.json`

Review result: all 16 rows accepted. Each image shows one decorated African king or queen in a strong three-quarter sovereign silhouette, plain low-detail background, culturally grounded regalia, controlled natural or supernatural symbolism, and close HOI4 painted leader readability. No councils, delegations, crowds, interiors, battle scenes, text artifacts, or modern props were present.

Technical result: all 16 DDS files are one-level uncompressed BGRA, `156x210`, `131168` bytes, `DDSCAPS_TEXTURE`, alpha extrema `(255,255)`, and byte-decoded pixel-equal to the processed PNG. The parent should only verify the existing `.gfx` registrations in `interface/012_africa_priority_member_characters.gfx`; no sprite rename is required.
