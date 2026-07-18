# Utopia Balance to Assignment — Built-in ImageGen Prompts

Use case: `stylized-concept`.

Asset type: compact HOI4 scripted-GUI threshold animation source frame.

Shared invariants for every call:

- People-free and text-free.
- Front-on orthographic camera, fixed framing, no perspective drift.
- One late-1930s civic balance and institutional measuring instrument in aged brass, dark bronze, blackened steel, parchment-beige highlights, and very restrained oxblood details.
- Long, shallow 6.6:1 instrument centered in a square source canvas, with generous plain charcoal-black ledger backing above and below so a clean horizontal crop can be taken.
- No labels, numerals, letters, words, maps, hands, faces, people, silhouettes, flags, modern electronics, neon light, plastic, glass UI, watermark, or decorative border.
- The physical state change must be legible through combs, guide rails, cells, retainers, calibrated spacing, and token positions.
- Preserve the exact instrument identity, camera, backing, scale, materials, and palette from the referenced previous frame on edit calls.

## Authoritative call construction

Every accepted call combined the shared invariants above with the corresponding instruction below. Edit calls used the preceding handle recorded in `metadata/frame_provenance.md` as their image reference.

| Frame | Exact state instruction added to the shared invariants |
| --- | --- |
| 000 | Correct the supplied draft into one long, shallow, strictly front-on civic measuring rail. Remove any top-down drift and every extra token. Keep exactly five plain brass tokens at irregular positions, with the calibrated comb fully retracted. |
| 001 | Edit only the mechanism state: begin extending the calibrated brass comb from the central carriage until it touches the nearest token. Leave all five tokens irregular and preserve the instrument and camera. |
| 002 | Slide the outer guide rails inward and move exactly two tokens into the first measured cells. Preserve the comb extension and all fixed parts. |
| 003 | Extend the comb farther and move a second pair of tokens into adjacent measured positions, producing a visible aligned row while one token remains in transit. |
| 004 | Raise perpendicular dividers to turn the row into a shallow matrix and move the final loose token toward its cell. Preserve the front-on camera and physical materials. |
| 005 | Place all five tokens in separate visible cells with equal measured spacing while leaving every retainer open. Keep one intentionally empty sixth cell in the 2-by-3 matrix. |
| 006 | Close the small brass retainers around the five occupied cells and settle the central gauge level. Keep the matrix, tokens, and empty cell fixed. |
| 007 | Refine the reached Assignment state into a clean measured matrix: five uniformly spaced retained tokens, one empty cell, all retainers seated, and fixed front-on camera. It must remain a distinct authored state from frame 006. |

The accepted ImageGen handles, reference chain, source dimensions, and source/processed hashes are recorded in `metadata/frame_provenance.md`.
