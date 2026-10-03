# CSH flag load repair: asset subagent handoff

Status: complete; ready for parent review.

Scope delivered:
- Added the CSH base, democratic, neutrality, fascism, and communism flags at normal, medium, and small sizes (15 runtime TGAs total).
- Added generated source masters, the prompt and refinement record, 15 processed PNG previews, a master/size comparison contact sheet, a manifest, and a GFX handoff.
- No GFX, gameplay, history, localisation, or country files were edited. No stage or commit was made.

Design and source mode:
- Native ImageGen fictional institutional artwork for the stateless internal Scientific Office identity.
- One generated master is shared across the five filename aliases by design. The aliases are intentionally identical because CSH is an internal scientific holder rather than a political country identity.
- Source master: docs/assets/cbrn_scientist_holder_flags/source_png/csh_scientific_office_master.png (SHA-256 403d2e09062825a33d36bdf09b77e0877ffc63e5e2fc2e3a66d5415391f83652).
- Comparison sheet: docs/assets/cbrn_scientist_holder_flags/contact_sheets/csh_flags_master_and_sizes.png.

Reference and conversion evidence:
- Offline flag guidance read from paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md, Flag section, lines 461-480, offline reference revision 0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d: uncompressed 32-bit ARGB TGA, bottom-left origin, automatic filename lookup, and 82x52 / 41x26 / 10x7 sizes.
- Installed vanilla native flag-size definition: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_graphics.lua lines 938-945, SHA-256 dfdab0a5fad7319d7b5ac524d98af49d3a0c1f95772e6b7a76abce54836f3d86 (parent-supplied evidence).
- Canonical reference ladder inspected at .agents/skills/chaos-redux-event-assets/assets/gfx_references/flags/contact_sheet.png; the library identifies its flag families in README.md lines 44-46 and 58-61 and catalogs their provenance and sizes in CATALOG.md lines 107-129.
- CXT/KRG repository examples establish the same type 2, 32 bpp, 8-bit alpha descriptor, bottom-left origin. Vanilla C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/USA.tga establishes bottom-left origin at 10x7, 298 bytes.
- All final TGAs use image type 2, 32 bpp, descriptor 8, bottom-left origin, opaque alpha, exact payload length, and passed pixel-for-pixel decoded PNG comparisons. Per-file sizes and SHA-256 hashes are in the asset manifest.
- The connected HOI4 reference MCP routes were unavailable to this agent; local references and actual installed/repository assets supplied the required format evidence.
- No game session or fresh runtime warning evidence was produced; the user's live QA remains the runtime validation.

Asset package: docs/assets/cbrn_scientist_holder_flags/
GFX handoff: docs/assets/cbrn_scientist_holder_flags/gfx_handoff.md
Manifest: docs/assets/cbrn_scientist_holder_flags/manifest.md
