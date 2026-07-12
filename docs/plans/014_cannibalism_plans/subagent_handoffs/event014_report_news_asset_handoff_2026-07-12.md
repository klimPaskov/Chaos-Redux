# Event 014 Report and News Asset Handoff — 2026-07-12

## Outcome

The remaining seven aftermath/Wendigo report images and the public Wendigo news image have independent generated sources, processed finals, package DDS copies, runtime DDS textures, contacts, prompt provenance, hashes, and GFX mappings.

The tranche emphasizes active containment, escape, assault, rescue, network movement, and public panic. The transformed leader and packs are physically feral and immediately distinct from ordinary human portraits. The custody images are post-reveal only.

## Changed files and identifiers

- Package: `docs/assets/014_cannibalism/report_news_imagegen/`
- Runtime: `gfx/event_pictures/014_cannibalism/`
- Processor: `docs/assets/014_cannibalism/report_news_imagegen/process_report_news_assets.py`
- Manifest: `docs/assets/014_cannibalism/report_news_imagegen/manifest.md`
- GFX handoff: `docs/assets/014_cannibalism/report_news_imagegen/gfx_handoff.md`
- Prompt ledger: `docs/assets/014_cannibalism/report_news_imagegen/prompts/generation_ledger.md`
- Validation: `docs/assets/014_cannibalism/report_news_imagegen/validation/report_news_asset_validation.tsv`
- Final contact: `docs/assets/014_cannibalism/report_news_imagegen/contact_sheets/report_news_processed_contact_sheet.png`

The exact eight sprite identifiers and paths are listed in `gfx_handoff.md` and its TSV equivalent. Existing GFX registrations already use those exact identifiers and paths, so no interface edit was required for this tranche.

## Meaningful validation

- Eight unique source hashes and eight unique normalized final pixel hashes.
- Seven 210x176 report images and one 397x153 news image.
- The news final is verified true monochrome.
- All runtime files decode as opaque, one-level, uncompressed BGRA DDS textures.
- Package/runtime DDS hashes match for every asset.
- The processed and runtime-decoded contact sheets were visually reviewed as a full set.

## Simplifications, omissions, and blockers

None within this tranche. One futuristic countdown draft was rejected and regenerated as grounded period apparatus; it is retained only as audit provenance.
