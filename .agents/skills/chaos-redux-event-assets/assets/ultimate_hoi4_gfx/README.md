# Curated Ultimate HOI4 GFX companion

This skill-local collection contains a reviewed subset of [Globvs/Ultimate-HOI4-GFX](https://github.com/Globvs/Ultimate-HOI4-GFX/tree/3626dc83c8573d6603fa497138090b04b64a15ba), pinned to commit `3626dc83c8573d6603fa497138090b04b64a15ba`. It complements the canonical Vanilla HOI4 reference library at `../vanilla_reference/`; it does not establish engine canvas, sprite, or UI behavior.

Start with [CATALOG.md](CATALOG.md), then inspect the contact sheet and individual original in the relevant folder:

- [Focus pieces](focus_pieces/contact_sheet.png): transparent motifs for composition and style study.
- [Focus backgrounds](focus_backgrounds/contact_sheet.png): frame and emblem arrangements for study; final focus subjects still come from ImageGen.
- [National spirit and decision category backgrounds](national_spirit_backgrounds/contact_sheet.png): study all; only rows marked `background_template` may be composited under original ImageGen art after exact consumer review.
- [Portrait backdrops](portrait_backdrops/contact_sheet.png): style references under the existing portrait source-mode and identity gates.

Local filenames use lowercase snake_case. CATALOG maps each to its original upstream path, canvas, transparency, role, SHA-256 and credit. Paired PSDs retain editable layers but are not final runtime art. Paint.NET files remain available at the [pinned upstream revision](https://github.com/Globvs/Ultimate-HOI4-GFX/tree/3626dc83c8573d6603fa497138090b04b64a15ba/Focus%20Backgrounds/Frames%20for%20Paint.NET); they are not part of this curated local set.

The `decision_category_background_blue_roundel.png` is approved as a decision-category backdrop candidate. The catalog also approves `spirit_background_circle`, `spirit_background_rectangle`, `spirit_background_ring`, and `spirit_background_shield` as persistent idea or national-spirit backdrop candidates. Approval to composite a backdrop does not fix the final canvas or replace the consumer-specific sprite and alpha review. Focus backgrounds and portrait backdrops in this collection remain references.

The upstream [CREDITS.txt](CREDITS.txt) says contributors consented to free use; no SPDX LICENSE is present. Individual contributors are not identified per file in the pack. Credit the collection and any individually verified creator in the output manifest. Preserve the template layer separately from ImageGen subject art and final processed PNG/DDS. Do not wire these library files directly into runtime GFX.
