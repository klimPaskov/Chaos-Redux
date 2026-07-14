# Event 015 ideology flag-variant handoff

Date: `2026-07-14`  
Mode: asset production only

## Outcome

The four incomplete route families now have deliberate files for every HOI4 ideology lookup. This pass adds `12` stems and `36` runtime TGAs. Together with the existing route flags, Event 015 now has `25` stems at all three engine sizes: `75` runtime flag files.

No existing valid flag was overwritten. No gameplay, localisation, interface, specification, or spreadsheet file was edited. Flags require no `.gfx` registration.

## Added stems

- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism`
- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality`
- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism`
- `UTOPIA_MANIFESTO_COUNCIL_UNION_democratic`
- `UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality`
- `UTOPIA_MANIFESTO_COUNCIL_UNION_fascism`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND_communism`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality`

Each stem is installed at:

- `gfx/flags/<stem>.tga` — `82x52`
- `gfx/flags/medium/<stem>.tga` — `41x26`
- `gfx/flags/small/<stem>.tga` — `10x7`

## Design and provenance

The twelve source masters are original fictional `image_gen` outputs made in twelve separate calls. Each call used only the matching route's existing base master as visual reference. The designs preserve route identity while changing composition, not merely palette:

- Voluntary Commonwealth: communal foundation, sheltered civic diamond, and stepped guarded hierarchy.
- Council Union: open chamber, balanced registers, and command-chevron tool assembly.
- Planned Utopia: open civic survey, common-table survey, and vertical survey monument.
- Closed Island: separated gateways, equal shared boundary, and balanced controlled channel.

Practical Commonwealth was used only as the structural precedent for a complete ideology family; none of its artwork was copied. No real national, party, fascist, or extremist symbol appears in the new designs.

## Package files

- Source PNGs: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/flags/`
- Processed PNGs: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/processed_png/flags/`
- Package TGAs: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/final_tga/flags/`
- Decoded inspection PNGs: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/decoded_png/flags/`
- Canonical manifest: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/manifest.md`
- Prompt record: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/prompts/route_identity_prompts.md`
- GFX handoff: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/gfx_handoff.md`
- Deterministic build/validation tool: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/_tooling/build_identity_flag_variants.py`

## Review sheets

- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/ideology_flag_variants_source_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/ideology_flag_variants_decoded_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/ideology_flag_variants_size_ladder_decoded_contact_sheet.png`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/flags_decoded_contact_sheet.png`

## Validation evidence

- Focused report: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/ideology_flag_variant_validation.json`
- Checksum ledger: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/ideology_flag_variant_checksums.sha256`
- Full-package report: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/validation.json`
- Coverage is exactly five route stems × unsuffixed plus four ideologies × three sizes: `75` flag TGAs.
- All TGAs are uncompressed image type `2`, `32` bits per pixel, descriptor `8`, bottom-left origin, with fully opaque alpha.
- Dimensions are exactly `82x52`, `41x26`, and `10x7`; byte lengths and Pillow decodes match the processed PNGs.
- Package and runtime copies are byte-identical.
- Each route has `4/4` unique ideology hashes, and the twelve new main-size designs are `12/12` unique.
- The only intentional duplicates in the full set are the four pre-existing unsuffixed/canonical ideology aliases.

## Parent and auditor follow-up

No wiring edit is required for these flags. The parent should retain all `75` installed flag files when assembling or committing Event 015. The country-package auditor can use the focused validation report and size-ladder contact sheet for independent coverage and visual review.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Existing valid assets overwritten: none.
- Missing ideology variants: none.
- Blockers or known risks: none.
