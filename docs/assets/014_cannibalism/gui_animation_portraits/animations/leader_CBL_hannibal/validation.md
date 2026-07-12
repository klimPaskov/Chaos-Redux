# leader_CBL_hannibal Validation

## Mechanical results

- Source frames: 12 present, 12 distinct SHA-256 hashes
- Source dimensions returned by built-in imagegen: 1080x1456, 1082x1454, or 1086x1449
- Processed frames: 12 present, 12 distinct SHA-256 hashes, all exactly 156x210
- Static PNG: 156x210 and byte-identical to processed frame 000
- Sheet PNG: 1872x210, exactly 12 horizontal 156-pixel columns
- GIF: 12 frames, 170 ms per review frame, infinite loop; review only
- Adjacent processed-frame mean absolute pixel difference: minimum 11.01, average 16.71, maximum 22.17 on an 8-bit channel scale
- Adjacent changed-pixel ratio above threshold: minimum 29.20%, average 41.68%, maximum 52.55%
- Last-to-first loop difference: mean absolute difference 10.68, changed-pixel ratio 25.99%
- Static DDS: 156x210, pitch 624, 32-bit BGRA masks `00FF0000/0000FF00/000000FF/FF000000`
- Sheet DDS: 1872x210, pitch 7488, the same 32-bit BGRA masks
- Both DDS files decode pixel-identically to their source PNGs

## Visual results

- The 156x210 contact sheet preserves the skull, both hands, tongue, unequal eyes, long crooked face, ruined period clothing, and dark-crimson staining.
- The action reads in order: clutch, lift, tongue approach, first contact, drag, socket sweep, crown apex, pull-away, second lap, lower, swallow, return.
- No source or processed frame reads calm, actor-like, classically framed, or like a CBA warlord reuse.
- Every frame visibly redraws jaw, tongue, hand anatomy, skull angle, eye direction, shoulders, stains, and cloth; there is no transform-only or locally composited motion.
- The first and final frames are similar enough to loop while remaining separately generated and hash-distinct.

## Reveal secrecy

- The early and warlord scripted-GUI surfaces are explicitly pre-reveal.
- The revealed portrait window requires `cannibalism_reveal_complete`.
- The reveal effect sets the public flag before recruiting `CBL_hannibal`.
- The package contains no pre-reveal alias, generic warlord portrait, or GUI-static substitute.

## Scope and exclusions

- No GFX, GUI, gameplay, localisation, audio, static GUI artwork, shared/root manifest, or protected legacy portrait was edited.
- No placeholder, sourced third-party image, actor likeness, ancient-general/Carthaginian/Punic/elephant/classical framing, or cultural/sacred motif is present.
