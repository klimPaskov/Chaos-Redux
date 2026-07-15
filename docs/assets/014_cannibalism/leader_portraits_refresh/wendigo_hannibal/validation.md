# Event 014 Wendigo Hannibal validation

## Package checks

- Independent static source and processed master: present.
- Animation source frames: 16 present, 16 unique SHA-256 hashes.
- Processed frames: 16 present, 16 unique SHA-256 hashes, all 156x210.
- Sheet PNG: 2496x210; all 16 sliced segments match their corresponding processed frame pixel-for-pixel.
- Review GIF: 16 frames, infinite loop, 2,670 ms total duration, effective 5.993 fps; the in-game sprite remains exactly 6 fps.
- Static and sheet DDS round trips decode pixel-identically to their processed PNG masters.

## Motion checks

Adjacent-frame mean absolute pixel differences are all nonzero, confirming that no frame is duplicated. The measured range is 3.258-21.780. The final two transitions measure 15.369 for 014→015 and 21.780 for 015→000, distributing the return-to-rest change across the generated bridge instead of concentrating it in one snap. The aggregate source and final contact sheets were visually reviewed and accepted.

## DDS checks

- Static DDS: `DDS ` magic, 124-byte legacy header, 156x210, uncompressed 32-bit colour, opaque alpha, 131,168 bytes.
- Sheet DDS: `DDS ` magic, 124-byte legacy header, 2496x210, uncompressed 32-bit colour, opaque alpha, 2,096,768 bytes.
- Static SHA-256: `bb9e1fcb96c63b064a7432f03810ac8dfef103ef335b6f5e9470e44b0ab7bd16`.
- Sheet SHA-256: `54cce739991daf690ed1d077a6da510a52e4404020e1197aa7373f0c87d356af`.
- Preserved legacy SHA-256 before and after delivery: `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`.

## Registration checks

`interface/014_cannibalism.gfx` retains two static sprite names and one 16-frame animated sprite pointing to the delivered filenames. No GFX or GUI source was edited.
