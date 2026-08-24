# March Predation Column v8 ImageGen prompt

## Initial faithful edit

Use case: background-extraction

Asset type: exactly one Meshy 7 image-to-3D character reference for a Hearts of Iron IV custom unit

Input images: Image 1 is the sole edit target and authoritative visual source.

Primary request: isolate only the main foreground painted archer from Image 1 as one complete, clean, colored character on a genuinely transparent alpha canvas. Remove the sky, landscape, and the extra figure at lower left. Upscale and clean compression while preserving the source character with extremely high fidelity.

Subject invariants: preserve the exact same main character identity, face, body proportions, muscular anatomy, broad crouched archer pose, gaze, braided hair, face and body paint, bow, arrow, bowstring, quiver, arrows, clothing, bracers, necklaces, palette, materials, silhouette, and all source-visible details. Keep the bow fully visible and readable, the quiver and arrows fully visible, and both hands clearly interacting with the bow exactly as in the source.

Allowed additions only: add one small crude bone close weapon, visibly sheathed at the belt; add only restrained, non-cultural cannibal bone trophies integrated as a few simple bone/tooth pieces at the belt or necklace. These additions must be secondary and must not obscure the bow, quiver, hands, limbs, or silhouette.

Framing: one subject only, centered, complete head-to-toe character with generous transparent padding, no crop, no ground shadow, no scenery, no base, no text.

Cultural constraint: do not identify or redesign the subject as any real or living community; do not add sacred motifs, real-world regalia, ethnographic markers, or culturally specific symbols. Preserve the existing fictional paint and clothing without naming or extending their cultural meaning.

Avoid: do not re-pose, modernize, knightify, restyle, beautify, masculinize, change anatomy, change body paint, change clothing, replace the bow, alter the quiver, add armor, add modern tactical gear, add scenery, add a second person, add gore, add text, add watermark, add opaque or checkerboard background, add halos, matte edges, internal alpha holes, or cast-shadow remnants. Do not substantially redesign anything beyond the explicitly allowed small sheathed bone weapon and restrained bone trophies.

Output requirement: real transparency in unused canvas; clean alpha edges; fully colored single image suitable as the only Meshy input.

Result: blocked by ImageGen output moderation under request id `b49a8842-024f-482d-bbd9-bae5ecea4561`.

## Parent-approved moderation-only retry

The parent approved one narrow exception: add only a minimal rough opaque distressed leather or hide chest harness or wrap for moderation, preserving the original physique, paint, pose, silhouette, bow, quiver, clothing palette, and identity. It must not become armor or modern clothing.

The successful retry repeated every identity, pose, equipment, palette, cultural-neutrality, framing, and no-redesign invariant above, added the approved minimal chest wrap, and retained only the already-authorized small sheathed bone weapon and restrained bone or tooth trophies.

## Targeted transparency/framing repair

Change only the background and framing. Remove the baked checkerboard entirely and replace unused canvas with genuine transparent alpha. Expand the canvas so the right boot and every part of the character, bow, bowstring, arrow, quiver, and clothing are fully visible. Preserve every subject detail from the successful moderation retry. Reconstruct only the tiny clipped tip of the right boot consistently with the visible boot.

Result: complete framing, but ImageGen again returned baked RGB checkerboard. The documented fallback used installed `rembg 2.0.61` post-processed masking followed by `evidence/process_checker_alpha_v8.py` to remove and decontaminate only the remaining neutral-white boundary fringe.
