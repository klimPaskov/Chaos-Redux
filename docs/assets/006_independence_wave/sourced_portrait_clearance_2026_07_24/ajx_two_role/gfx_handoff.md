# AJX two-role source-only GFX handoff

This handoff is source-only and does not edit any `.gfx` file.

## PASS civic source

Consumer: `AJX_friedrich_hoffmann`.

Grounded identity: Walter Simons.

Use the exact crop at `source_crops/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.png` after the parent completes normal DDS conversion and licence attribution review.

Suggested large sprite name: `GFX_portrait_AJX_friedrich_hoffmann_civic_large`.

Suggested texture path after parent conversion: `gfx/leaders/AJX/AJX_friedrich_hoffmann_civic_large.dds`.

Do not infer or create a `_small` texture from this package without a separate parent-approved conversion step.

Source: [Bundesarchiv Bild 102-12279, Walter Simons](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg).

Attribution: `Bundesarchiv, Bild 102-12279 / CC-BY-SA 3.0`.

## HOLD military source

Consumer: `AJX_karl_becker`.

Grounded identity: Hans Eberhard Kurt von Salmuth.

The exact archival crop is `source_crops/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.png`.

Suggested large sprite name if the parent explicitly accepts the visual-era caveat: `GFX_portrait_AJX_karl_becker_commander_large`.

Suggested texture path after parent approval and conversion: `gfx/leaders/AJX/AJX_karl_becker_commander_large.dds`.

This candidate is HOLD because the NARA source is a 1947–1948 courtroom portrait rather than a 1936 military-uniform portrait.

Do not wire or convert this candidate until the parent resolves that HOLD.

Source: [NARA Catalog 167824751 / High Command Trial portrait](https://catalog.archives.gov/id/167824751).

Commons source page: [Hans von Salmuth, defendant in High Command Trial](https://commons.wikimedia.org/wiki/File:Hans_von_Salmuth,_defendant_in_High_Command_Trial.jpg).

Rights basis: United States federal-government work, public domain under 17 U.S.C. §105.

## Evidence files

The full source, provenance, rights, ownership, date, era-fit, hash, and rejection record is `manifest.md` and `manifest.json`.

The decoded-pixel equality proofs are `metadata/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.json` and `metadata/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.json`.
