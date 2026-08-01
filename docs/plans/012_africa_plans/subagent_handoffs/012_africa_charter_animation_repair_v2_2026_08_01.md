# Event 012 Africa charter animation repair v2 handoff

Status: complete for the two requested animated scripted-GUI packages.

The prior independent frame sequence was rejected and is not used. Both rebuilt sequences use one locked ImageGen master per asset and separately authored ImageGen edits for each planned overlay state. Deterministic processing applies the locked master alpha silhouette and center anchor to every frame, assembles the horizontal sheet, creates the review GIF/contact sheet, and converts the approved PNGs to uncompressed BGRA DDS. No transform/filter-only motion was used.

## Charter seal activation

- Sprite IDs remain `GFX_012_africa_charter_seal_activation_animated` and `GFX_012_africa_charter_seal_activation_static`.
- Source frames: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/source_frames/charter_seal_activation_000_source.png` through `_007_source.png`.
- Processed frames: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/processed_frames/charter_seal_activation_000.png` through `_007.png`, all exactly 64x64.
- Frame plan and brief: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/frame_plan.md` and `brief.md`.
- Sheet PNG: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/sheets/charter_seal_activation_sheet.png` at 512x64.
- Sheet DDS: `gfx/interface/012_africa/animations/charter_seal_activation_sheet.dds` at 512x64.
- Static PNG: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/sheets/charter_seal_activation_static.png` at 64x64.
- Static DDS: `gfx/interface/012_africa/animations/charter_seal_activation_static.dds` at 64x64.
- Review GIF: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/previews/charter_seal_activation_preview.gif` (8 fps review-only).
- Contact sheet: `docs/assets/012_africa/charter_ui/animations/charter_seal_activation/previews/charter_seal_activation_contact.png`.
- Manifest, gfx handoff, validation, and checksums: the sibling `manifest.md`, `gfx_handoff.md`, `notes/validation.md`, and `notes/checksums.sha256` files in that package.

The sequence progresses from a dormant protected seal through staged gold star/ring ratification to a fully activated resting seal. The contact sheet shows one stable Africa-shaped center silhouette and one stable eight-star radial geometry across all frames.

## Charter authority ring

- Sprite IDs remain `GFX_012_africa_charter_authority_ring_animated` and `GFX_012_africa_charter_authority_ring_static`.
- Source frames: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/source_frames/charter_authority_ring_000_source.png` through `_009_source.png`.
- Processed frames: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/processed_frames/charter_authority_ring_000.png` through `_009.png`, all exactly 64x64.
- Frame plan and brief: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/frame_plan.md` and `brief.md`.
- Sheet PNG: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/sheets/charter_authority_ring_sheet.png` at 640x64.
- Sheet DDS: `gfx/interface/012_africa/animations/charter_authority_ring_sheet.dds` at 640x64.
- Static PNG: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/sheets/charter_authority_ring_static.png` at 64x64.
- Static DDS: `gfx/interface/012_africa/animations/charter_authority_ring_static.dds` at 64x64.
- Review GIF: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/previews/charter_authority_ring_preview.gif` (6 fps review-only).
- Contact sheet: `docs/assets/012_africa/charter_ui/animations/charter_authority_ring/previews/charter_authority_ring_contact.png`.
- Manifest, gfx handoff, validation, and checksums: the sibling `manifest.md`, `gfx_handoff.md`, `notes/validation.md`, and `notes/checksums.sha256` files in that package.

The sequence progresses by authority threshold from ten subdued delegate nodes through staged node infill and linked-track activation to a complete high-authority ring. The contact sheet shows one stable ten-node ring construction, fixed node positions, and an empty center across all frames.

## QA evidence

- Canonical reference inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/factions/contact_sheet.png` plus individual faction logo plates. Reference art is review-only.
- Geometry evidence: `notes/*_geometry_metrics.json` reports identical master alpha masks on every processed frame for both assets.
- DDS evidence: `docs/assets/012_africa/charter_ui/animations/dds_pixel_parity.json` reports exact PNG-to-DDS pixel parity, valid legacy BGRA headers, exact lengths, declared dimensions, and alpha range 0–255 for all four runtime DDS files.
- Runtime paths match the existing `interface/012_africa_charter.gfx` registrations exactly. Existing `.gfx`, `.gui`, scripted GUI, triggers, gameplay, localisation, and spreadsheet files were not edited.
- No generic, vanilla-resized, static-only, transform-only, unrelated-center, or 3D fallback was used.
