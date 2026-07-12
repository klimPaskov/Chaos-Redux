# leader_ZZZ_hannibal_wendigo Validation

## Mechanical results

- Source frames: 16 present, 16 distinct SHA-256 hashes
- Source dimensions returned by built-in imagegen: 1080x1456, 1080x1457, 1081x1455, or 1082x1454
- Processed frames: 16 present, 16 distinct SHA-256 hashes, all exactly 156x210
- Static PNG: 156x210 and byte-identical to processed frame 000
- Sheet PNG: 2496x210, exactly 16 horizontal 156-pixel columns
- GIF: 16 frames, 170 ms per review frame, infinite loop; review only
- Adjacent processed-frame mean absolute pixel difference: minimum 19.29, average 25.46, maximum 30.93 on an 8-bit channel scale
- Adjacent changed-pixel ratio above threshold: minimum 47.70%, average 57.54%, maximum 63.30%
- Last-to-first loop difference after the frame-015 replacement: mean absolute difference 7.93, changed-pixel ratio 14.27%
- Static DDS: 156x210, pitch 624, 32-bit BGRA masks `00FF0000/0000FF00/000000FF/FF000000`
- Sheet DDS: 2496x210, pitch 9984, the same 32-bit BGRA masks
- Both DDS files decode pixel-identically to their source PNGs

## Visual results

- One identity persists through all 16 source and processed frames: elongated bald skull, crooked nose, familiar scar line, torn ears, large pale left eye, smaller dark right eye, and irregular teeth.
- The figure remains dramatically inhuman throughout. Even return frames retain unequal anatomy, long claw, asymmetric shoulders, frost-split skin, and a feral expression.
- The separate action reads in order: crouch, tracking, neck jerk, claw unfurl, jaw unhinge, diagonal spring, farthest reach, snap, apex, recoil, reverse whip, swallow, shoulder collapse, jaw rethread, re-crouch, return.
- The replacement final frame matches the starting silhouette closely enough for a clean loop while remaining a separate full imagegen render and SHA-distinct.
- No frame contains antlers, horns, deer traits, animal skull headdress, sacred symbol, ritual circle, runes, totem, dreamcatcher, feathers, beadwork, ceremonial regalia, tribal motif, or living Indigenous motif.
- No frame contains an actor likeness, ancient-general/Carthaginian/Punic/elephant/classical framing, skull-lick action reuse, placeholder, or transform-only motion.

## Reveal secrecy

- The Wendigo command window requires `cannibalism_reveal_complete`, `cannibalism_wendigo_route_active`, and the transformed Hannibal country trigger.
- The package contains no pre-reveal alias, no generic early-header sprite, and no public name or text.

## Scope and exclusions

- No GFX, GUI, gameplay, localisation, audio, static GUI artwork, shared/root manifest, or protected legacy portrait was edited.
- No locally generated particles, glow pulses, warped still, or composited anatomy was used.
