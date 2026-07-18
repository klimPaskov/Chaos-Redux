# Validation report

Status: **pass**.

## Human visual review

All ten accepted cards were inspected at generated-source scale, after
external-matte removal, at native `300x96`, at 2x nearest-neighbour scale, and
after decoding the runtime DDS.

- No accepted card contains a person, face, hand, body, silhouette, flag,
  readable text, letters, numerals, signature, watermark, or pseudo-writing.
- No accepted card contains a malformed seal, compass, gear, institution,
  hourglass, or other visibly stretched geometry.
- All four borders remain complete after the small aspect crops. Target
  Selected and Ultimatum Available use fresh 3.0:1 sources instead of the
  rejected tall canvases.
- Each state reads independently through a different authored pictogram,
  object arrangement, border language, and accent palette.
- The left and centre remain calm and dark enough for live GUI copy. Important
  state symbols remain confined to the right.
- The processed PNG and DDS-decoded contact sheets are visually identical.

Primary review surfaces:

- `contact_sheets/case_cards_post_matte_source_contact_sheet.png`
- `contact_sheets/case_cards_processed_contact_sheet.png`
- `contact_sheets/case_cards_decoded_contact_sheet.png`
- `native_size_review/case_cards_native_plus_2x_nearest.png`
- `contact_sheets/case_cards_rejected_aspect_contact_sheet.png`

## Task-specific automated validation

`tooling/validate_case_cards.py` recorded these results in
`metadata/validation_report.json`:

- exactly ten accepted and three rejected ImageGen handles;
- ten distinct accepted source hashes, processed hashes, runtime DDS hashes,
  and RGBA pixel hashes;
- a built-in C2PA assertion in every accepted source master;
- maximum accepted post-matte aspect delta of 4.0%;
- content-safe cover crops followed by uniform scaling for every state;
- quiet-field luminance means at or below 35 and standard deviations at or
  below 6 across the live-copy region;
- right-side pictogram standard deviations at or above 15;
- minimum pairwise mean absolute error of 19.604 across right-side state
  regions, confirming distinct treatments;
- exact `300x96` processed and decoded dimensions;
- exact processed-PNG to DDS RGBA pixel equality;
- legacy 128-byte DDS header, one level, uncompressed BGRA8, 1200-byte pitch,
  fully opaque alpha, and 115328-byte file length for every runtime asset;
- one-to-one stable GFX texture bindings and GUI icon blocks at `(8,4)` for
  all ten stems.

## Scope and blockers

No simplification, placeholder, fallback, missing state, unwired runtime file,
or unresolved asset blocker remains in this package. No `.gfx`, `.gui`,
scripted GUI, gameplay, or top-level asset-authority document was edited by
this asset task.

