# Event 014 March Predation Column — Chiveli recovery v9 ImageGen prompts

## Primary bounded edit

Use case: precise-object-edit

Asset type: single full-body Meshy image-to-3D reference for a fictional horror-game cannibal archer

Input image: the attached Alexander Chiveli *Cannibal* Sketchfab render is the sole edit target and identity reference.

Primary request: preserve the exact same single fictional humanoid character, body anatomy and proportions, tall crazed stance, red-painted skin pattern, horned bone-and-metal jaw mask, ragged brown armor and cloth, one large close-combat axe, and overall recognizable silhouette. Replace only the smaller second axe in the character's right hand with a crude culturally neutral shortbow of rough dark wood and hide wrapping, held clearly and fully visible. Add a compact visible back quiver with several arrows. Add only a few modest culturally neutral bone trophies tied to existing belt/armor straps; do not create sacred, ethnographic, tribal, or living-community motifs. Keep the original close axe in the other hand.

Scene/backdrop: isolate exactly one full-body character on genuine transparent alpha; no floor, no base, no environment, no shadow, no glow, no matte, no text, no watermark.

Composition/framing: centered frontal three-quarter/full-body view, all horns, hair streamers, bow, axe, quiver, cloth, hands, and both feet completely inside the canvas with comfortable transparent margin. Improve character size/readability relative to the source thumbnail while retaining the pose and silhouette.

Style/medium: faithful polished modern stylized 3D game-character render matching the source materials and identity, not a new design.

Constraints: change only the second weapon and the explicitly requested quiver/arrows plus minimal bone trophies; preserve face/mask, horns, anatomy, pose, red body paint, armor construction, clothing palette, remaining axe, identity, and silhouette. Do not redesign, modernize, knightify, culturally anchor, add another character, add gore, add a display base, or crop any equipment. Output must contain real transparent pixels outside the subject.

## Targeted transparency retry

Use case: background-extraction

Primary request: remove only the baked gray-and-white checkerboard background from the preceding generated cannibal archer image and replace it with genuine transparent alpha pixels.

Constraints: preserve every character pixel, color, edge, body proportion, pose, red paint, horned jaw mask, hair streamers, armor, cloth, bone trophies, large axe, shortbow, bowstring, quiver, arrows, hands, and feet exactly as shown; do not redraw, restyle, reposition, crop, relight, sharpen, add, or remove anything on the subject. Preserve the full canvas and comfortable margin. No floor, base, shadow, glow, matte, halo, text, watermark, or visible checker pattern. Output must have real transparent pixels outside the subject.

## Result and alpha route

Both native ImageGen outputs were 24-bit RGB with a baked checkerboard and alpha 255 throughout. The second output was retained because it preserved the source identity and requested equipment most faithfully. The fallback processor `evidence/process_checker_alpha_chiveli_v9.py` uses seeded checker/foreground segmentation, retains the bounded pale abdominal highlight, decontaminates newly visible fringe RGB, and applies a narrow antialiased alpha edge. The resulting RGBA input at exact SHA-256 `9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289` was parent-approved on 2026-08-24 and promoted to `refs/original/meshy_input.png`; provider submission remains blocked on the receipt-based verifier ownership fix and exact gate pass.
