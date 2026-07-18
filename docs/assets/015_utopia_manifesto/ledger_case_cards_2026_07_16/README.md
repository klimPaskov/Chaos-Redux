# Event 015 Necessary Ground case cards

This package supplies the ten missing live-state cards for Event 015's
Necessary Ground Ledger panel. Every accepted state has an independent
built-in ImageGen source master, a mechanically finished 300x96 PNG, an
uncompressed one-level BGRA8 runtime DDS, and a decoded verification PNG.

## Package index

- `manifest.md` — accepted state and runtime inventory.
- `provenance.md` — generation, reference, rejection, and processing history.
- `geometry_decisions.md` — post-matte aspect measurements and per-card crop
  decisions.
- `validation_report.md` — human review and task-specific automated checks.
- `gfx_gui_handoff.md` — stable sprites, runtime paths, position, and priority.
- `prompts/exact_imagegen_prompts.md` — exact prompts for ten accepted and
  three rejected generations.
- `metadata/source_handles.json` — built-in ImageGen handles, timestamps,
  references, prompts, source paths, and SHA-256 values.
- `metadata/processing_report.json` — mechanical processing and DDS header
  details per accepted state.
- `metadata/validation_report.json` — machine-readable validation results.
- `metadata/binary_checksums.sha256` — SHA-256 inventory for source, review,
  processed, decoded, and runtime binaries.
- `contact_sheets/` and `native_size_review/` — source, rejection, processed,
  decoded, native, and 2x-nearest review surfaces.
- `tooling/` — prompt extraction, mechanical finishing, review layout, and
  validation scripts.

Runtime files live in `gfx/interface/015_utopia_manifesto/ledger/`. Existing
GFX and GUI wiring consumes the stable stems documented in
`gfx_gui_handoff.md`.

