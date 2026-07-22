# AJX grounded source retry

This is the 2026-07-22 source package for the two Event 006 Saar grounded
portrait gaps. It is deliberately separate from runtime `gfx/` and contains
no gameplay or GFX edits.

- **Leader candidate:** Johannes Hoffmann, Nationaal Archief/Anefo CC0 source
  (1955; `needs_user_review` because the image is after the 1936 scenario).
- **Commander candidate:** Willy Schmelcher, 1938 archival book portrait,
  Commons public-domain record (`source_ready`).
- **Outputs:** unchanged JPEG masters, explicit 156x210 PNG crops, legacy
  uncompressed BGRA DDS files, source/crop contact sheet, manifest, ownership
  ledger, and deferred GFX handoff.

Start with [manifest.md](manifest.md). The parent implementation agent must
review the Hoffmann era gap, Schmelcher's SS/police context, and the identity
transfer before copying either DDS to a runtime path.

