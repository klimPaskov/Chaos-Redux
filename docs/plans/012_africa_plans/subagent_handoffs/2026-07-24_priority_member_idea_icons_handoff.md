# Event 012 Africa priority-member idea icon handoff

Status: complete for the bounded 35 registered idea textures. This handoff is owned by the icon asset tranche and does not modify `.gfx`, gameplay, localisation, portraits, flags, focus icons, decision icons, event images, or catalog files.

## Runtime output

All 35 final textures are in `gfx/interface/ideas/012_africa/priority_members/` at exact 60x68 dimensions. The existing registrations in `interface/012_africa_priority_member_assets.gfx` already provide the sprite names and texture paths, so the main agent does not need a `.gfx` edit. The complete id-to-sprite-to-path table is in `docs/assets/012_africa_priority_member_idea_icons/crosswalk.md`.

The package contains the shared settlement trio (`council_settlement`, `civic_settlement`, `producer_settlement`) plus separately authored problem and mature states for Asante, Oyo, Sokoto, Kanem-Bornu, Manden, Kongo, Buganda, Aksum, Harar, Kilwa, Nubia, Luba, Lunda, Great Zimbabwe, Merina, and Zulu. Mature sources are independent ImageGen generations, never recolors, filters, transforms, or crops of the problem source.

## Evidence

- Source PNGs: `docs/assets/012_africa_priority_member_idea_icons/source_png/` (35).
- Processed PNGs: `docs/assets/012_africa_priority_member_idea_icons/processed_png/` (35, alpha extracted and fitted to 60x68).
- Keyed intermediates: `docs/assets/012_africa_priority_member_idea_icons/validation/keyed/` (35).
- DDS-decoded PNGs: `docs/assets/012_africa_priority_member_idea_icons/validation/dds_decoded/` (35).
- Contact sheets: `contact_sheets/source_contact_sheet.png`, `contact_sheets/processed_contact_sheet.png`, and `contact_sheets/decoded_dds_contact_sheet.png`.
- Prompt and visual provenance: `docs/assets/012_africa_priority_member_idea_icons/prompt_provenance.md`.
- Requirement crosswalk and exact sprites: `docs/assets/012_africa_priority_member_idea_icons/crosswalk.md`.
- Asset manifest: `docs/assets/012_africa_priority_member_idea_icons/manifest.md`.
- DDS evidence: `validation/dds_validation.json` records legacy header fields, exact file length, alpha range, SHA-256 hashes, and decoded-pixel equality for every texture; all 35 are header-valid and pixel-equal.
- Registration evidence: `validation/path_resolution.json` records all 35 registered idea paths and resolves each to an existing DDS (`all_resolve: true`).

## Visual review notes

The canonical vanilla idea contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png` was inspected before generation. The final contact sheets show compact isolated silhouettes with transparent corners and high-contrast painted highlights. Problem/mature pairs use different source compositions and distinguish fractured infrastructure or administration from linked, functioning systems. The Asante problem source was regenerated after review to remove all stool, throne, seat, sacred-regalia, and damaged-cultural-object imagery; the accepted composition uses divided mundane ledgers, a split administrative seal, failed transport lines, and a closed civic chamber. The mature Asante source likewise uses mundane ledgers, gold ingots, linked transport lines, and an open civic chamber with no sacred object.

## Validation command

From the mod root, rerun `python -B docs/assets/012_africa_priority_member_idea_icons/validation/validate_and_decode.py` and `python -B docs/assets/012_africa_priority_member_idea_icons/validation/resolve_paths.py` after any asset replacement. DDS conversion used `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed.png> --output <runtime.dds> --width 60 --height 68`.

No blockers or fallback assets remain in this bounded icon package.
