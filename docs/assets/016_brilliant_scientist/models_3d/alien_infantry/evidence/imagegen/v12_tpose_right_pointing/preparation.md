# Alien Infantry V12 T-pose reference preparation

Status: reference-only candidate; not sent to Meshy and not promoted to runtime.

The edit target was `refs/original/meshy_input_v11_two_hand_firearm.png` with SHA-256 `CFF2E684F0D7D50A01084CEA76F2BA22CC4CF11BEB5D48AD829AD733FA2976D1`.

Native ImageGen was used first to change only the pose: a full-body neutral T-pose with both arms horizontal, the alien's right hand holding the existing ray pistol, and the pistol pointing horizontally toward the image's right edge.

The first ImageGen output baked a checkerboard into opaque pixels and was rejected.

A targeted background-extraction pass preserved the pose and design and produced the selected derivative with genuine alpha; the generated source was `C:\Users\klimp\.codex\generated_images\019f6063-512e-7170-84a3-5218017722b1\exec-c0909acf-6b08-4c16-a647-b2e514bdcf30.png`.

The workspace copy is `refs/original/meshy_input_v12_tpose_right_pointing.png` with SHA-256 `D2896A1D9B6C78BC5ED00268DDAC58928E871A9FF4816AE5BB0BC03C856B3036` and 1,195,428 bytes.

The output is 1024x1536 RGBA with alpha range 0–254, 1,382,054 fully transparent pixels, and no fully opaque pixels because ImageGen retained a soft anti-aliased edge; visual review confirms the background is transparent rather than a baked checkerboard.

The derivative preserves the alien's large black eyes, bald head, slim uniform, collar, belt, cuffs, boots, ray-pistol design, right-hand grip, and complete muzzle. The left arm is intentionally extended and empty to match the requested T-pose; later firearm-animation review must independently re-check the support-hand gate.

Exact preparation prompt:

> Use case: precise-object-edit / stylized-concept. Asset type: single Meshy-ready full-body character reference. Input image: Image 1 is the edit target and must remain the same alien character and same retro ray-pistol design. Create one faithful derivative only. Change only the pose and presentation: place the complete alien in a neutral full-body T-pose with both arms extended straight horizontally at shoulder height; the alien's right hand must hold the existing ray pistol, with the pistol barrel and circular muzzle pointing exactly horizontally toward the image's right edge. Keep the left arm extended and empty, with no second weapon. Preserve the exact alien face, large black eyes, bald head, slim proportions, uniform, shoulder collar, belt, cuffs, boots, ray-pistol silhouette, materials, palette, and distinctive details. Keep the complete body and complete pistol visible, with no cropping, no weapon duplication, no floating weapon, no strap, no extra figures, no text, and no redesign. Use a clean studio cutout with genuine transparency, not a painted checkerboard or opaque backdrop. This is a source-preserving Meshy reference preparation, not a new character design.

Second-pass background prompt:

> Use case: background-extraction. Asset type: transparent Meshy-ready character reference. Preserve the character, T-pose, body proportions, clothing, boots, face, ray pistol, right-hand grip, and the pistol pointing horizontally to the image's right exactly as shown. Change only the background treatment: remove every checkerboard square and replace it with genuine transparent alpha. Do not paint white, gray, black, or checkerboard pixels behind the subject. Do not alter the pose, weapon, silhouette, colors, materials, or framing. Keep the complete body and pistol uncropped, with clean alpha edges and no halo, text, or extra objects.
