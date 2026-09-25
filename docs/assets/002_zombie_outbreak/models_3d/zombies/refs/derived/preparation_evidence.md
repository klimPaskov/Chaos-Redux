# Base Zombie Reference Preparation Evidence

Candidate 02 is the selected reference candidate for parent/user review; user approval is still required before any Meshy submission.

## Candidate lineage and selection

- Candidate 01 was generated as an original source-free image, then rejected by the user with the exact feedback: “no, looks too human”.
- Candidate 01 remains unchanged at `refs/derived/imagegen_candidate_01.png`, with SHA-256 `843CDC9D40F0E8FF442517EB8A0E700D9E0BD6C772EC37B98D8D32C5AE830A19`; its prompt and rejected status are retained in `refs/derived/candidate_01_rejected_manifest.json`.
- Two targeted edit attempts on candidate 01 were blocked by ImageGen’s output safety filter (`violence`), request ids `076247a8-14a1-4b7f-9f43-c9028fcc39b7` and `de6694aa-2978-46ce-a9f8-4d573651f528`; neither produced an image.
- Candidate 02 was then generated as a fresh text-only source-free original, not as an edit of candidate 01.
- `refs/derived/imagegen_candidate_02.png` and `refs/original/meshy_input.png` are byte-identical; both have SHA-256 `3723991B3EFC92D573CA1CB94CDC6177EB1D501EE5F207DB1613D4E50C3EB3BB`.
- The exact candidate 02 prompt, provenance, attempt record, and approval states are in `refs/original/input_manifest.json`.

## Image and alpha review

- Candidate 02 is a 1024 × 1536 RGBA PNG, 1,860,254 bytes.
- Decoded alpha ranges from 0 to 254: 1,110,440 pixels are fully transparent and 462,424 have partial alpha; all four canvas corners have alpha 0.
- Its non-zero alpha bounding box is `(45, 11, 956, 1512)` with right and bottom coordinates exclusive. The maximum alpha of 254 is unchanged from the generated output.
- `refs/derived/alpha_checkerboard_candidate_02.png` is flattened QA evidence only, not a provider input; SHA-256 is `03119EBEB9C7793199E5EA96E1493325607FEBEC01C9ABE7521830C5F8067BE1`.
- Candidate 02 shows one unmistakably undead full-body civilian with a gaunt face, darkened eye sockets, cloudy eyes, a slack mouth with visible teeth, mottled gray-green skin, and thin clawlike but complete hands.
- It retains conventional biped anatomy, a symmetric rig-friendly A-pose, empty separated hands, separated legs, both visible shoes, and muted period civilian clothing.
- Producer and parent visual review found the checkerboard transparency clean and the figure suitable for the reference stage.

## Provenance and approval boundary

- Source mode is `source_free_user_authorized`. No historical or modern image, existing art, mesh, or screenshot was used as an artistic source; source search and source-to-refinement comparison do not apply.
- User authorization covers creation of the source-free reference. User review of candidate 02 and approval of the 64-credit Meshy ceiling remain pending before provider submission.
- No Meshy key/route/balance check, Meshy task, Blender route, rigging, animation, or paid provider operation was invoked. Meshy credits estimated and consumed are both 0.
- Provider use status is `needs_user_review`.