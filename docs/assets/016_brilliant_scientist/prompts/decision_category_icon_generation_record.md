# Event 016 decision and decision-category icon generation record

Date: 2026-07-24

Source mode: built-in `$imagegen` atlas generation followed by retained, non-transformative tile crops. The generated source atlases are `source_png/decision_icons/decision_icons_atlas_01_source.png`, `source_png/decision_icons/decision_icons_atlas_02_source.png`, and `source_png/decision_categories/decision_categories_atlas_source.png`.

The two decision prompts requested exact 5-column by 4-row grids of twenty distinct hand-painted 1930s–1940s Hearts of Iron IV decision emblems each. The first atlas covers foundation repair, power relay, rail and port, supply, laboratory hardening, prototype press, staff, scientific assembly, publication, compartmentalization, security assignment, relocation, invitation, archive theft, sabotage, protection, project approval, project suspension, independent replication, and charter negotiation. The second atlas covers confinement, assassination, military seizure, clone growth, robot assembly, paleogenetic hatchery, xenobiological vat, portal terminal, temporal anchor, alien laser cohorts, biological quarantine, singularity component, singularity arming, controlled disarmament, archive recovery, staff rotation, facility hardening, emergency containment, foreign extraction, and project-unit deployment.

The category prompt requested an exact 5-column by 2-row grid of ten distinct round category emblems: foundation administration, security and logistics, clone and machine, paleogenetics, xenobiology, portal and temporal, exotic and biological safeguards, foreign policy, integration, and terminal program.

Retained atlas SHA-256: decision atlas 01 `9B29745B3B30892FD70BE49A8C4ADF86810F57203293BA40EAAF5815E560A8BA`; decision atlas 02 `10B2C08EFEAB998E29AEF34A8947649F95C5331E4B5F427F7A7472242A722305`; category atlas `9795E5F9591F22A4B57DDF1B125673AFF7858E123191A63B3AE2D44EBC791742`.

All prompts required no text, letters, numerals, flags, watermarks, or UI, and required distinct silhouettes rather than recolors or focus-icon resizes. The canonical vanilla decision and decision-category contact sheets were inspected before generation. Cropped source masters remain in the package for provenance; `package_records/build_decision_category_icons.py` records crop bounds and performs only alpha-key extraction, exact-size normalization, and DDS conversion after generation.

Transparent processing used the official `remove_chroma_key.py` helper with border auto-key, soft matte, edge contract 1, and despill. The final runtime textures use the repository `convert_to_dds.py` converter and are validated as one-level uncompressed BGRA DDS.

Review sheets:

- `contact_sheets/decision_icons_016_sources_contact_sheet.png`
- `contact_sheets/decision_icons_016_processed_contact_sheet.png`
- `contact_sheets/decision_icons_016_decoded_dds_contact_sheet.png`
- `contact_sheets/decision_categories_016_sources_contact_sheet.png`
- `contact_sheets/decision_categories_016_processed_contact_sheet.png`
- `contact_sheets/decision_categories_016_decoded_dds_contact_sheet.png`

The machine-readable asset manifest, hashes, and crop-derived provenance are in `package_records/decision_category_icon_manifest.json`. Assignment coverage is in `package_records/decision_assignment_ledger.tsv` and `package_records/decision_category_assignment_ledger.tsv`.
