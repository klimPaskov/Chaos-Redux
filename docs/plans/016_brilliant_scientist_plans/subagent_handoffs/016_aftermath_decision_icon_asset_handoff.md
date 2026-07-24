# Event 016 aftermath decision icon asset handoff

Status: complete asset tranche; no commit or staging performed.

The qualifying-defeat aftermath package contains exactly 22 distinct decision icons at 32x32 and exactly 4 distinct decision-category icons at 50x40. All runtime DDS paths and sprite identifiers match the parent contract and the already-registered `interface/016_brilliant_scientist_aftermath_decisions.gfx` blocks.

## Runtime outputs

Decision DDS files are under `gfx/interface/decisions/016_brilliant_scientist/aftermath/decisions/`:

- `aftermath_found_scientific_commission.dds`
- `aftermath_exchange_countermeasures.dds`
- `aftermath_codify_personhood_and_asylum.dds`
- `aftermath_ban_singularity_components.dds`
- `aftermath_ratify_scientific_compact.dds`
- `aftermath_register_recovered_facility.dds`
- `aftermath_inventory_project_templates.dds`
- `aftermath_secure_command_archives.dds`
- `aftermath_certify_global_dismantlement.dds`
- `aftermath_rebuild_laboratory_state.dds`
- `aftermath_open_survivor_clinics.dds`
- `aftermath_build_memorial_archive.dds`
- `aftermath_close_reconstruction_board.dds`
- `aftermath_hear_clone_communities.dds`
- `aftermath_audit_machine_nodes.dds`
- `aftermath_secure_paleogenetic_reserves.dds`
- `aftermath_receive_xenobiological_handlers.dds`
- `aftermath_map_portal_terminals.dds`
- `aftermath_reconcile_temporal_records.dds`
- `aftermath_open_biological_archive.dds`
- `aftermath_catalogue_alien_cache.dds`
- `aftermath_dispose_singularity_core.dds`

Category DDS files are under `gfx/interface/decisions/016_brilliant_scientist/aftermath/categories/`:

- `aftermath_treaty.dds`
- `aftermath_inspection.dds`
- `aftermath_reconstruction.dds`
- `aftermath_remnants.dds`

The ready-copy sprite/path blocks for all 26 assets are in `docs/assets/016_brilliant_scientist/aftermath_decision_icons/package_records/aftermath_sprite_blocks.txt`; no `.gfx` file was edited in this tranche.

## Contrast revision record

Parent visual review rejected the first-pass first-atlas source because its first twelve decisions were too dark at native 32x32. The rejected source is preserved at `docs/assets/016_brilliant_scientist/aftermath_decision_icons/source_png/decisions/rejected/aftermath_decisions_atlas_01_rejected_first_pass_source.png` with SHA-256 `F8F33BCC571E17AA738CF9BA94B4A9851898C5C03F8C9B53C710667A1CB439B8`.

An intermediate image-generation revision is preserved at `source_png/decisions/revisions/aftermath_decisions_atlas_01_revision_01_source.png` with SHA-256 `060DE8D2BE5564BA12824CB8A99C59F52D8B1A32B9F8EB72C2E63074BC5CDF8E`. The final revision was regenerated with large bright central silhouettes and stronger ivory/brass/teal midtone separation rather than a brightness-only post-process. The current source atlas has SHA-256 `4A648A69FFC2C005DAA592B1B6B1B47C55701A3D94EF3B9A475B71E4AE86004C` and is documented in `package_records/aftermath_generation_record.md`.

The exact stable runtime filenames and sprite identifiers were preserved. The accepted last ten decision sources and all four category sources were unchanged; the deterministic rebuild regenerated their downstream alpha/PNG/DDS/decoded/contact outputs without changing their source content.

## Evidence package

All source masters, per-icon source crops, keyed alpha PNGs, processed target-size PNGs, decoded DDS PNGs, and contact sheets are isolated under `docs/assets/016_brilliant_scientist/aftermath_decision_icons/` in `source_png/`, `alpha_png/`, `processed_png/`, `dds_decoded_png/`, and `contact_sheets/`.

Machine records are in `package_records/`:

- `aftermath_decision_category_manifest.json` — 26 asset records with exact paths, sizes, rationales, and SHA-256 hashes.
- `aftermath_assignment_ledger.tsv` — 22 decision assignments.
- `aftermath_category_assignment_ledger.tsv` — 4 category assignments.
- `aftermath_sprite_blocks.txt` — exact parent sprite/path blocks.
- `aftermath_generation_record.md` — image-generation, crop, chroma-key, normalization, and DDS provenance.
- `build_aftermath_icons.py` and `validate_aftermath_icons.py` — reproducible isolated build/validation scripts.

## Validation

`python -B docs/assets/016_brilliant_scientist/aftermath_decision_icons/package_records/validate_aftermath_icons.py` returned after the contrast revision:

```json
{"assets": 26, "decisions": 22, "categories": 4, "assignment_rows": 22, "category_assignment_rows": 4, "status": "ok"}
```

The validator also checks unique source hashes, no orphan or duplicate ledger sprites, exact PNG dimensions and alpha corners, exact uncompressed BGRA DDS headers/payload lengths, and decoded-DDS pixel identity against processed PNGs. Detailed output is in `validation/aftermath_validation_report.json` and `validation/aftermath_validation_details.tsv`.

## Visual review and scope boundary

Processed and decoded contact sheets were inspected for crop integrity, transparent backgrounds, and semantic separation. The first twelve decisions were regenerated with bright central silhouettes and stronger midtone/highlight separation for native 32x32 readability; final visual acceptance remains a parent/user review item. The remnants package preserves distinct clone, machine, paleo, xeno, portal, temporal, biological, alien, and singularity silhouettes without text, numerals, flags, logos, watermarks, or modern electronics.

Only the isolated aftermath asset directories, runtime DDS files, and this handoff were changed. Gameplay, localisation, `.gfx`, `.gui`, spreadsheets, focus/idea/event files, shared manifests, and prior KRG icon assets were not edited.

## Parent review disposition

Parent visual review accepted the revised package after comparing the final source, processed 32x32, and decoded-DDS decision sheets and the unchanged source, processed 50x40, and decoded-DDS category sheets.

The regenerated first twelve icons retain immediately readable gold, ivory, and teal silhouettes on the dark decision-panel background; the ten remnant icons and four categories remain distinct; alpha edges are clean; and decoded DDS output is visually identical to the processed PNGs. All 26 assets are accepted for their exact registered consumers.
