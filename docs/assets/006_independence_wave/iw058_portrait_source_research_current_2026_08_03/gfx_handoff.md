# IW-058 ASY portrait source-only GFX handoff

This handoff is intentionally non-wiring. It gives the parent a source-locked portrait candidate without choosing a runtime basename or editing any `.gfx`, character, localisation, event, or gameplay file.

## Candidate

- Subject: Yousef VI Emmanuel II Thomas, Chaldean Catholic Patriarch of Babylon.
- Candidate preview: `processed_png/ASY_concordat_council_yousef_emmanuel_ii_thomas_156x210_source_placeholder.png`.
- Source master: `source_masters/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_hathitrust.jpg`.
- Exact crop and equality evidence: `source_crops/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.png` and `crop_metadata/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.json`.
- Comparison evidence: `review/ASY_yousef_emmanuel_ii_thomas_source_candidates_contact_sheet.png`.

## Wiring boundary

- `runtime_authorized = false`.
- `dds_created = false`.
- Parent did not supply a runtime basename, so this handoff does not invent one.
- Do not point a sprite or character at this package's `docs/assets` path. If the parent accepts the source and supplies the runtime basename, the parent must copy/convert the source-placeholder PNG through the repository-standard DDS path and own `.gfx` and character wiring.
- No GFX, character, localisation, event, focus, decision, history, or gameplay files were edited in this pass.

## Review gate

The source candidate remains `needs_user_review`. Commons records a `PD-US-expired` assertion and credits the 1921 *Shall this nation die?* scan, but the underlying image author is not identified. This is usable archival provenance for review, not a universal rights guarantee. The alternate 1925 Commons scan remains unselected because its author is unknown and its `PD-old` claim is less explicit.
