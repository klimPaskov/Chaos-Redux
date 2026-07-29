# Charter Ledger Core Icon Provenance

Source mode: generated symbolic icon using the built-in ImageGen tool required by `chaos-redux-event-assets` and the official `imagegen` skill.

Generation date: 2026-07-29.

Canonical reference inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/contact_sheet.png` and the individual decision references in that folder.

Prompt direction: hand-painted HOI4 vanilla decision-icon style; an open legal ledger with stitched spine and parchment pages; a sealed brass clause clasp; a simplified continent-wide Africa outline stamped into the right page; short abstract clause lines without readable text; restrained indigo, brass, parchment, and earth palette; centered isolated composition; no people, flags, weapons, crowns, religious symbols, watermark, or UI text; flat `#ff00ff` chroma-key background for removal.

Transparency processing: `remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`, followed by deterministic Lanczos resize to 32x32 RGBA.

| File | Dimensions / mode | SHA-256 |
|---|---|---|
| `source_png/decision_012_africa_charter_ledger_source.png` | 1254x1254 RGB | `3e7ccf53c757eb1a9e15c15e230df6ac9789fed8d9c973395641f4149353ae25` |
| `processed_png/decision_012_africa_charter_ledger.png` | 32x32 RGBA | `4a10e66e998d8f572d834d5f10d3f98f1e510c463a18d958e76f2e1b57f3e9de` |
| `gfx/interface/decisions/012_africa/core/decision_012_africa_charter_ledger.dds` | 32x32 BGRA DDS, 4224 bytes | `57b88f60eff6d0a2cc8537baf153173146218d72cf1ebbc4b9de4340bbad40b0` |

The generated source is retained in the package so provenance remains reviewable even after the runtime DDS is wired.
