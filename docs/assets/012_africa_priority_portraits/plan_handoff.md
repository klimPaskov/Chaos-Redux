# Event 012 Africa sovereign portrait production handoff

Scope delivered: the accepted 16-polity sovereign portrait family with stable `*_sovereign` source, processed, DDS, decoded, manifest, crosswalk, provenance, validation, and contact-sheet evidence.

Completed production chain:

1. Retained the eight accepted sovereign source/processed masters already present in the package and admitted them to the runtime folder.
2. Generated and visually reviewed the missing Harar, Kilwa, Nubia, Luba, Lunda, Great Zimbabwe, Merina, and Zulu sovereign masters with the built-in ImageGen workflow.
3. Produced all 16 opaque `156x210` processed PNGs with the repository leader processor.
4. Produced all 16 runtime DDS textures with the repository converter and decoded every DDS back to PNG for parity checks.
5. Rebuilt the all-16 sovereign contact sheets and visually inspected source, processed, and decoded-DDS columns.
6. Rebuilt `metadata/sovereign_provenance.json`, `metadata/sovereign_dds_validation.json`, and `metadata/sovereign_package_audit.json` for all 16 rows.
7. Removed obsolete council artifacts only from this owned Event 012 asset/runtime package. No gameplay, interface, localisation, event, focus, specification, spreadsheet, or political-route file was changed.

Current accepted file sets for every key (`asante`, `oyo`, `sokoto`, `kanem_bornu`, `manden`, `kongo`, `buganda`, `aksum`, `harar`, `kilwa`, `nubia`, `luba`, `lunda`, `great_zimbabwe`, `merina`, `zulu`):

- `source_generated/portrait_012_africa_priority_<key>_sovereign_source_gen.png`
- `source_png/portrait_012_africa_priority_<key>_sovereign_source.png`
- `processed_png/portrait_012_africa_priority_<key>_sovereign.png`
- `comparison/dds_decoded/portrait_012_africa_priority_<key>_sovereign.png`
- `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_<key>_sovereign.dds`
- `metadata/012_africa_priority_<key>_sovereign_processing.json` where present for the source processor run

The parent owns `.gfx` registration and character wiring. The exact stable sprite-to-texture handoff is in `gfx_handoff.md`, and requirement coverage is in `crosswalk.md`.
