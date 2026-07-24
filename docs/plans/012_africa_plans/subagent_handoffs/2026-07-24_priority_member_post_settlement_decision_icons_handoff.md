# Event 012 post-settlement decision icon handoff

Status: complete for the bounded 16 registered post-settlement decision textures.

## Runtime output

Final DDS files are in `gfx/interface/decisions/012_africa/priority_members/` and preserve the exact sprite names and texture paths already registered in `interface/012_africa_priority_member_assets.gfx`. Target size follows the existing decision-icon precedent: 32x32 pixels, one-level uncompressed BGRA DDS with alpha.

The 16 icons cover Asante, Oyo, Sokoto, Kanem-Bornu, Manden, Kongo, Buganda, Aksum, Harar, Kilwa, Nubia, Luba, Lunda, Great Zimbabwe, Merina and Zulu continuing settlement actions. Subjects are distinct and grounded in their post-settlement play: producer boards, market corridors, pastoral governance, water/caravan covenants, river/road projects, cross-border rights, federal arbitration, heritage/Red Sea treaties, trade/water security, customs/ports, Nile rights, mining labour, cross-border citizenship, land/heritage restoration, island federalism, and land/labour reconstruction.

## Evidence

- Source PNGs: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/source_png/` (16).
- Processed PNGs: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/processed_png/` (16, 32x32 alpha).
- Keyed intermediates: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/validation/keyed/` (16).
- DDS-decoded PNGs: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/validation/dds_decoded/` (16).
- Contact sheets: `contact_sheets/source_contact_sheet.png`, `contact_sheets/processed_contact_sheet.png`, and `contact_sheets/decoded_dds_contact_sheet.png`.
- Prompt/provenance: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/prompt_provenance.md`.
- Requirement crosswalk: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/crosswalk.md`.
- Manifest: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/manifest.md`.
- GFX handoff: `docs/assets/012_africa_priority_member_post_settlement_decision_icons/gfx_handoff.md`.
- DDS evidence: `validation/dds_validation.json` reports `count: 16`, all complete legacy headers and decoded-pixel equality.
- Registration evidence: `validation/path_resolution.json` reports `registered_post_settlement_paths: 16` and `all_resolve: true`.

## Visual review notes

The canonical vanilla decision contact sheet was inspected before generation. The source and decoded contact sheets show compact object silhouettes at 32x32 with transparent corners and strong HOI4 contrast. No icon uses a sacred symbol as an invented authenticity claim. Asante uses mundane boards, ledgers and a civic canopy only; Aksum and Great Zimbabwe use generic heritage/stone infrastructure rather than sacred text or relics; Buganda, Zulu, Sokoto and Luba avoid crowns, sacred objects and readable scripts.

No placeholders, fallbacks, recolors, transform-only variants, or gameplay/registration edits were made.
