# Event 006 Pacific focus-icon family handoff

Date: 2026-07-18
Subagent scope: bounded visual production only
Status: complete; parent-owned `.gfx` registration and focus-script references are wired in the shared workspace

## Deliverable

Created the requested 14 unique national-focus icons: seven HBX California and seven HAW Hawaiʻi. Every row has a distinct built-in ImageGen source, processed transparent PNG, final runtime DDS at the exact user-provided path, source/final hashes, native and enlarged contact-sheet review, and copy-ready base/`_shine` sprite blocks.

Package source of truth: `docs/assets/006_independence_wave/pacific_focus_icons_2026_07_18/`

- `manifest.md` — requirement crosswalk, visual identity notes, scope boundary, validation summary.
- `prompts/006_pacific_focus_icon_prompts.md` — retained per-icon ImageGen subject prompts and shared constraints.
- `source_png/focuses/` — 14 original chroma-key source PNGs.
- `processed_png/focuses/` — 14 94x86 transparent processed PNGs.
- `contact_sheets/006_pacific_focus_icons_source_contact_sheet.png` — source review.
- `contact_sheets/006_pacific_focus_icons_1x_contact_sheet.png` — native 94x86 checkerboard review.
- `contact_sheets/006_pacific_focus_icons_3x_contact_sheet.png` — 3x nearest-neighbour review.
- `validation/validation.json` — per-row source/processed/runtime hashes and full DDS header/dimension/alpha evidence.
- `validation/hashes.sha256` — flat SHA-256 ledger.
- `gfx_handoff.md` — exact 28 copy-ready `.gfx` spriteType blocks and parent-owned wiring notes.
- `_tooling/build_pacific_focus_icons.py` — reproducible chroma-removal, canonical focus fit, contact-sheet, DDS conversion, and header-validation script.

Runtime DDS files are installed under `gfx/interface/goals/006_independence_wave/` using the exact stable filenames from the parent prompt. All files are 94x86, uncompressed legacy BGRA8888 with alpha, one level, exact 32,464-byte payloads.

## Stable sprite IDs

The 14 base IDs and paired `_shine` IDs are in the package handoff. They intentionally omit any trailing `_focus` and use the exact provided names. Each `_shine` sprite points to its own base icon texture and `gfx/FX/buttonstate.lua`.

The current Pacific focus implementation now uses these exact IDs. The parent or Pacific focus re-audit agent owns `.gfx` registration; no existing `.gfx` file was edited by this tranche. The dedicated new registry is `interface/006_independence_wave_pacific_focus_icons.gfx`.

## Reference/style analysis

Inspected the canonical `icons/national_focus` reference folder and contact sheet before generation. The family shows centered symbols with bold silhouettes, transparent corners, warm aged-gold edging, cool steel/navy bodies, controlled painterly depth, and native-size readability. The generated family follows that finish while avoiding copied vanilla symbols.

HBX motifs are deliberately distinct: screened arsenal gates/crates with a restrained bear-seal medallion, coastal supply ledger, Sacramento civic dome/table, ports-factory-guard triad, federal asset ledger, procurement-board industrial seal, and three-route maritime congress. HAW motifs avoid invented sacred/universal symbolism: shipping register, coastwatch tower/binoculars/lantern, representative compact table, inter-island supply/coastwatch network, base/property ledger and keys, bounded autonomy mandate, and diplomatic delegation ship/table.

## Validation and review

- All 14 source images were generated individually through built-in ImageGen and retained.
- All 14 source chroma-key fields were removed with the official `remove_chroma_key.py` helper using soft matte, edge contract, and despill.
- All processed corners are fully transparent; no key-green field remains.
- Every DDS passed magic/header, BGRA masks, texture caps, exact dimensions, exact file length, and alpha min/max checks recorded in `validation/validation.json`.
- Native 94x86 and 3x enlarged contact sheets were visually inspected. Parent visual review on 2026-07-18 marked both sheets PASS: distinct, readable, and coherent with canonical HOI4 focus art.

## Scope boundary and omissions

No gameplay scripts, localisation, `.gfx`, `.gui`, portraits, flags, characters, advisors, ideas, decisions, tech, event pictures, spreadsheets, or protected BAY/RHI/HBX/FSM portrait assets were touched. There are zero Event 006 advisor icon outputs, references, or placeholders. No fallback, recolour, resized shared icon, or generic substitute was used.

## Parent follow-up

1. Preserve the exact 14 base + 14 `_shine` registrations in `interface/006_independence_wave_pacific_focus_icons.gfx`.
2. Preserve the seven HBX and seven HAW focus references using the matching base sprite IDs.
3. Preserve runtime paths and names; do not add `_focus` suffixes or redirect to shared Event 006 art.
