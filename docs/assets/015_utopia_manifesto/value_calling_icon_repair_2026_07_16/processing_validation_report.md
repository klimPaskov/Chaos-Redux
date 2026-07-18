# Event 015 Ledger Value and Calling Icon Processing and Validation Report

## Outcome

The frozen 5x2 ImageGen atlas produced ten distinct runtime Ledger icons: four `32x32` Value icons and six `48x48` Calling icons. The processed PNGs and decoded DDS files visually match, retain real alpha, and preserve the ImageGen-authored brass-and-teal emblem artwork.

## Reference and size review

The required offline wiki set was consulted, including Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On Actions, Event Modding, Decision Modding, Idea Modding, AI Modding, Interface Modding, and Scripted GUI Modding. The Interface Modding guidance confirms that `iconType` points to a registered `spriteType`.

The canonical skill reference library and its extended icon contact sheet were inspected. Direct vanilla precedents included the `48x48` military-raid outcome icon and MIO department icon, plus a `32x32` state-modifier icon and their owning `.gfx` definitions. Native dimensions remain surface-specific, so the current Event 015 handoff and requirement-to-runtime crosswalk take precedence:

- four Value icons: `32x32`;
- six Calling icons: `48x48`.

No focus or decision icon was resized to satisfy either GUI family.

## Deterministic processing

The retained script is `_tooling/process_value_calling_icons.py`.

1. Refuse any atlas whose SHA-256 differs from `7a1704f1c6d720ff72b9cdc3715101361bb8b836033607d0ff244dbb31c7d440` or whose canvas differs from `1774x887`.
2. Divide the exact source canvas proportionally into five columns and two rows. The resulting source boxes are recorded in `source_records.json`.
3. Save every raw source cell separately before transparency processing.
4. Run the installed ImageGen chroma helper with border sampling, soft matte, transparent threshold `12`, opaque threshold `220`, and despill.
5. Find only the surviving source-art alpha bounds, resize in premultiplied alpha with Lanczos, and center on the documented canvas with transparent edge space.
6. Write a legacy one-level uncompressed BGRA DDS with a 128-byte header, pixel format at byte `76`, `RGB | ALPHAPIXELS` flags `65`, BGRA channel masks, `DDSCAPS_TEXTURE` at byte `108`, and no mipmaps.
7. Copy the exact DDS bytes into the runtime folder, decode both package and runtime files, and compare their RGBA payloads to the processed PNG.
8. Build review-only contact sheets. Checkerboards and labels appear only on those review sheets, never in source, processed, or runtime art.

The processor does not draw or reconstruct visible art.

## Machine validation results

- asset count: `10`;
- unique raw source-cell SHA-256 hashes: `10`;
- unique processed PNG SHA-256 hashes: `10`;
- unique runtime DDS SHA-256 hashes: `10`;
- unique 256-bit perceptual dHashes: `10`;
- minimum pairwise perceptual Hamming distance: `55`;
- maximum pairwise perceptual Hamming distance: `89`.

For every processed and decoded icon:

- dimensions equal the documented native canvas;
- alpha minimum is `0` and maximum is `255`;
- all four canvas corners are fully transparent;
- both fully opaque and partially transparent pixels exist;
- no magenta-key pixel remains at alpha `32` or higher;
- the package DDS and runtime DDS are byte-identical;
- the decoded DDS pixels equal the processed PNG pixels;
- Pillow independently decodes the same pixels;
- every required legacy DDS header field and offset passes.

The four `32x32` DDS files are exactly `4,224` bytes each (`128 + 32 * 32 * 4`). The six `48x48` DDS files are exactly `9,344` bytes each (`128 + 48 * 48 * 4`). These lengths match the expected one-level uncompressed format and the corresponding native-size vanilla precedents.

## Visual inspection

The raw source-cell sheet shows ten separate ImageGen compositions without adjacent-cell contamination. The processed alpha sheet confirms centered silhouettes and no opaque magenta square. The decoded DDS sheet is visually identical to the processed sheet.

The Choice-versus-Assignment emblem remains neutral. Its bisected composition balances an open hand and branching choice motif against measuring tools and a records cabinet. Both sides use comparable scale, material, contrast, and framing; neither side receives a moral colour code, approval mark, punishment mark, or text label.

## Provenance finding

The atlas filename, frozen generated master, existing Event 015 handoffs, and accepted specification identify the source as built-in ImageGen art. The repository does not contain the verbatim original prompt for this atlas. `source_records.json` records that absence and does not substitute a reconstructed prompt. This is a provenance limitation, not an art-processing failure; the immutable source hash and every cell crop remain available for review.

## Interface boundary

This repair did not edit `.gfx`, `.gui`, scripted GUI, localisation, or gameplay. Matching stable sprite and consumer identifiers appeared in the shared working tree while the package was being processed; the parent agent retains responsibility for reviewing and finalising that wiring.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Omitted runtime assets: none; all four Values and all six Callings are present.
- Blockers: none for asset processing or handoff.
- Recorded provenance limitation: the original verbatim ImageGen prompt is not present in the repository.
