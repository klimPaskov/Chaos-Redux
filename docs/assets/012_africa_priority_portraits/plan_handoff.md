# Event 012 dramatic portrait production handoff

Scope delivered: replace all 16 rejected source-photo atmosphere portraits with genuinely fantastical, dramatic, period-grounded collective councils. The parent may wire the stable sprites without changing `.gfx` identifiers.

Completed production chain:

1. Built-in ImageGen generated one unique source master per polity, with the matching source package used only for architecture/material/polity grounding.
2. Parent visual review approved all 16 dramatic masters and the generated direction, including regenerated Asante, Oyo, Kanem-Bornu, Manden, and Luba candidates.
3. Repository leader processor produced opaque `156x210` processed PNGs.
4. Repository DDS converter produced 16 runtime textures; decoded parity and legacy BGRA header checks are recorded in `metadata/dds_validation.json`.
5. Current source/processed/DDS contacts, manifest, crosswalk, prompts, provenance, validation, and stable sprite handoff are present.

Current accepted file sets (all 16 keys: `asante`, `oyo`, `sokoto`, `kanem_bornu`, `manden`, `kongo`, `buganda`, `aksum`, `harar`, `kilwa`, `nubia`, `luba`, `lunda`, `great_zimbabwe`, `merina`, `zulu`):

- `source_generated/portrait_012_africa_priority_<key>_council_source_gen.png`
- `source_png/portrait_012_africa_priority_<key>_council.png`
- `processed_png/portrait_012_africa_priority_<key>_council.png`
- `comparison/dds_decoded/portrait_012_africa_priority_<key>_council.png`
- `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_<key>_council.dds`
- `metadata/portrait_012_africa_priority_<key>_council_processing.json`

Exact SHA-256 values for each source, canonical source copy, processed PNG, and DDS are in `metadata/dramatic_provenance.json`; exact DDS header, dimensions, length, alpha, and decoded output checks are in `metadata/dds_validation.json`.

Superseded material: the old atmosphere/crop/test outputs, old source-photo runtime results, old prompt records, and first-pass ImageGen handles are not current evidence. They remain untracked in the shared working tree only because cleanup is outside the safe shell policy; do not stage them. Stage the accepted current paths above plus `manifest.md`, `gfx_handoff.md`, `crosswalk.md`, `validation.md`, `plan_handoff.md`, `prompts/generated_prompt_records.md`, the two current metadata JSON files, and the three dramatic contact sheets.

No GFX, gameplay, localisation, GUI, or spreadsheet files were edited. Parent validation should confirm the 16 stable sprite paths in `interface/012_africa_priority_member_characters.gfx` resolve to the 16 DDS files listed above.
