# Utopia Balance to Choice — Built-in ImageGen Prompts

Use case: `stylized-concept`.

Asset type: compact HOI4 scripted-GUI threshold animation source frame.

Shared invariants for every call:

- People-free and text-free.
- Front-on orthographic camera, fixed framing, no perspective drift.
- One late-1930s civic balance and institutional measuring instrument in aged brass, dark bronze, blackened steel, parchment-beige highlights, and very restrained oxblood details.
- Long, shallow 6.6:1 instrument centered in a square source canvas, with generous plain charcoal-black ledger backing above and below so a clean horizontal crop can be taken.
- No labels, numerals, letters, words, maps, hands, faces, people, silhouettes, flags, modern electronics, neon light, plastic, glass UI, watermark, or decorative border.
- The physical state change must be legible through hinges, gates, channels, latches, detents, and token positions.
- Preserve the exact instrument identity, camera, backing, scale, materials, and palette from the referenced previous frame on edit calls.

## Authoritative call construction

Every accepted call combined the shared invariants above with the corresponding instruction below. Edit calls used the preceding handle recorded in `metadata/frame_provenance.md` as their image reference.

| Frame | Exact state instruction added to the shared invariants |
| --- | --- |
| 000 | Correct the supplied draft into one long, shallow, fully horizontal civic measuring rail. Remove every person-like pictogram and figure. Keep exactly three plain round brass tokens seated on one closed common rail, the central carriage closed, and all branch gates shut. |
| 001 | Edit only the mechanism state: lift the left latch and open the first small branch gate while all three tokens remain seated. Preserve the instrument, camera, crop room, backing, materials, and lighting. |
| 002 | Open a second hinged route from the center and move only the lead token clear of its detent. Keep the first gate open and preserve all fixed parts exactly. |
| 003 | Separate the mechanism into three clearly distinct route channels and move two tokens away from the common rail into separate branch mouths. Preserve the camera and instrument identity. |
| 004 | Fold the central divider fully down and place the three tokens at different open branch mouths with visible free space between them. Keep the route hardware physical and unglowing. |
| 005 | Extend the three brass route leaves farther, retract their stops, and advance each token independently along its own route. Preserve every completed change from frame 004. |
| 006 | Settle the three tokens on separate open rests with no clamp, cage, or grid holding them. Leave every route mechanism open and keep the carriage unlocked. |
| 007 | Refine the reached Choice state into a balanced branching tableau: three independent token positions, fully open route leaves, unlocked carriage, and fixed front-on camera. It must remain a distinct authored state from frame 006. |

The accepted ImageGen handles, reference chain, source dimensions, and source/processed hashes are recorded in `metadata/frame_provenance.md`.
