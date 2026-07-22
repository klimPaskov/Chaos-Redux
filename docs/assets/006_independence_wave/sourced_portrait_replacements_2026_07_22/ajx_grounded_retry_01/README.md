# AJX grounded source retry

This is the 2026-07-22 source and review package for the two Event 006 Saar
grounded portrait gaps. It is deliberately separate from runtime `gfx/` and
contains no gameplay or GFX edits.

- **Leader candidate:** Johannes Hoffmann, Nationaal Archief/Anefo CC0 source
  (1955; `needs_user_review` because the image is after the 1936 scenario).
- **Commander research evidence:** Willy Schmelcher, 1938 archival book
  portrait, Commons public-domain record (`role_mismatch_research_only`). He
  was a Saarbruecken police/SS chief, not an army corps commander, so this DDS
  must not be wired to `AJX_karl_becker`.
- **Commander search result:** Karl Becker is blocked by the vanilla live owner
  `GER_karl_heinrich_emil_becker` and weak corps-command role fit. Wilhelm
  Fahrmbacher is the strongest Palatinate/corps lead but has no rights-clear
  face-visible portrait source. No role-correct commander is source-ready.
- **Outputs:** unchanged JPEG masters, explicit 156x210 PNG crops, legacy
  uncompressed BGRA DDS files, source/crop contact sheet, manifest, ownership
  ledger, and deferred GFX handoff.

Start with [manifest.md](manifest.md). The parent implementation agent must
review the Hoffmann era gap and the role/ownership blockers before any identity
transfer or runtime copy. No ImageGen output was made in this retry.

