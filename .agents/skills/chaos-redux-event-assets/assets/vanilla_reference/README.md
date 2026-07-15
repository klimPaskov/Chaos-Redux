# Canonical vanilla visual references

This directory is the canonical, skill-local review library for
`chaos-redux-event-assets`. It contains a deliberately small selection of PNG
review copies extracted from the locally installed Hearts of Iron IV files.
They are style, framing, scale, transparency, and pipeline references only.

Do not wire these PNGs into Chaos Redux, copy the depicted people or symbols
into final art, or ship them as mod assets. For implementation, inspect the
original vanilla source and its `.gfx`, `.gui`, `.asset`, or `.mesh` precedent,
then create an original or properly sourced Chaos Redux asset.

## Provenance

- Installed game root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`
- Installed build at extraction: `Operation Postern v1.19.2.0.a729 (d245)`
- Extraction date: `2026-07-15`
- Review format: lossless RGBA PNG decoded from the source DDS or TGA
- Pixel policy: preserve the source texture canvas exactly; do not crop,
  stretch, repaint, or normalize transparent bounds during extraction
- Inventory: 51 reference PNGs in 20 leaf folders, covering 18 distinct asset
  categories, plus 4 contact sheets

Every PNG and its exact vanilla source path are listed in [CATALOG.md](CATALOG.md).

## Contact sheets

- `contact_sheets/portraits_and_flags.png` — leader portraits, advisor dossier
  icons, and three flat flags across the normal/medium/small ladder
- `contact_sheets/icons.png` — focus, idea, decision, mission, decision-category,
  achievement, officer-corps, technology, special-project, and balance-of-power
  icon families
- `contact_sheets/event_art.png` — report-event and news-event image formats
- `contact_sheets/units.png` — 2D equipment art, two-frame unit counters, and 3D
  model material references

The checkerboard is a review background, not part of the extracted image.

## Dimension rules

Native vanilla texture dimensions are evidence, not a universal resize order.
Always inspect the relevant vanilla `.gfx` definition and the existing Chaos
Redux precedent before producing a final asset.

- Leader portrait references are exactly `156x210`.
- Advisor dossier references are exactly `65x67`; they are separately composed
  cards, not resized leader portraits.
- Flags are shown at the full required ladder: `82x52`, `41x26`, and `10x7`.
  Final game flags remain uncompressed 32-bit TGA files with vanilla-compatible
  origin/header behavior; the PNGs here are review copies only.
- Vanilla focus references use `100x88` texture canvases. Visible artwork and
  transparent margins can differ from older nominal-size guidance.
- Idea, decision, decision-category, and technology textures have family- and
  file-specific native canvases. Preserve the intended in-game footprint and
  validate against the owning sprite rather than forcing one blanket size.
- Division counter references are `152x42` two-frame strips (`noOfFrames = 2`),
  giving two `76x42` frames.
- Equipment UI illustrations have variable native widths and are not division
  counters or map models.
- `units/model_material_refs_3d/` contains UV diffuse textures used by model
  meshes. These are material references, not 2D equipment icons, unit counters,
  rendered concept art, or finished model previews.

## Maintenance rule

Keep this library representative and allowlisted. Add an example only when it
documents a genuinely missing asset family, state, size, or engine pipeline.
Record the exact source and dimensions in `CATALOG.md`, rebuild the relevant
contact sheet, and never bulk-copy a vanilla directory.
