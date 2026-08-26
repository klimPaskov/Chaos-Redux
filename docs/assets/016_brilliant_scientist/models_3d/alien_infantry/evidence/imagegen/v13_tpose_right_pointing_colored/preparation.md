# Alien Infantry V13 colored firearm reference preparation

Status: reference-only candidate; not sent to Meshy and not promoted to runtime.

The edit target was `refs/original/meshy_input_v12_tpose_right_pointing.png` with SHA-256 `D2896A1D9B6C78BC5ED00268DDAC58928E871A9FF4816AE5BB0BC03C856B3036` and 1,195,428 bytes.

Native ImageGen was used for the requested object edit. The alien, full-body T-pose, clothing, face, framing, and right-hand grip were preserved while the ray pistol was enlarged by approximately 1.30x, rotated to a straight horizontal aim toward the image's right edge, and colorized with muted olive-green skin, charcoal/olive clothing, gunmetal and bronze weapon materials, and a restrained cyan emitter accent.

The first color edit was `C:\Users\klimp\.codex\generated_images\019f6063-512e-7170-84a3-5218017722b1\exec-2b752d21-ae09-468d-a459-c763d2d73b53.png`. It baked a checkerboard into opaque pixels and was rejected for Meshy use.

A second ImageGen background-extraction pass was `C:\Users\klimp\.codex\generated_images\019f6063-512e-7170-84a3-5218017722b1\exec-fc93d911-9baa-49e3-a9de-7b45f5611a45.png`. It supplied real alpha but retained a broad dark glow, so it was not copied directly.

As a narrow failed-native-alpha cleanup fallback, the colorized output was passed through an alpha-matte background removal and a conservative alpha-edge threshold. The cleanup source was `exec-2b752d21-ae09-468d-a459-c763d2d73b53.png`, the resulting temporary file was `alien_v13_alpha32.png`, and the workspace derivative is `refs/original/meshy_input_v13_tpose_right_pointing_colored.png`.

The selected workspace derivative is 1024x1536 RGBA, 758,184 bytes, SHA-256 `2D72EEB020C8989B463F214D4B5FC1C29C4AB313AEEE9F033B71E6DE1881BF3A`, with alpha range 0–255, 1,387,237 fully transparent pixels, and 181,038 fully opaque pixels. Corner pixels are fully transparent; white- and black-background composites were visually inspected for remaining checkerboard or glow contamination.

The enlarged pistol remains complete and uncropped, its emitter is horizontal, and its grip remains in the alien's right hand. The left arm remains extended and empty as requested; later firearm-animation review must independently re-check support-hand contact.

Exact ImageGen object-edit prompt:

> Precise object edit of the supplied alien infantry reference. Preserve the exact same full-body alien, face, anatomy, neutral T-pose, clothing, belt, boots, framing, and transparent background. Do not redesign the character and do not add a second hand, second weapon, text, logo, insignia, base, collage, or alternate view. Edit only the ray pistol and its color treatment: make the complete pistol approximately 1.30 times larger while keeping the grip firmly in the existing right hand and keeping the entire weapon and muzzle inside the canvas. Rotate the pistol in the image plane until the barrel axis is exactly horizontal, pointing straight toward the image right edge with no upward or downward tilt; keep the arm and hand position unchanged. Colorize the preserved reference with a restrained retro-futurist palette: muted moss/olive-green skin, deep charcoal and olive suit with subtle cool-gray panel highlights, and a larger metallic gun in gunmetal gray with dark bronze details and one restrained cyan energy accent at the emitter. Keep the result clean and readable for Meshy reference preparation. Preserve genuine transparent alpha around the subject; do not paint a checkerboard, white, gray, black, gradient, studio glow, or any other backdrop. Keep the full alien and enlarged horizontal pistol uncropped.

Exact ImageGen extraction prompt:

> Exact alpha-matte cleanup. Preserve every visible pixel of the colorized alien, clothing, face, T-pose, enlarged ray pistol, right-hand grip, straight horizontal barrel, colors, scale, and framing. Change only the background and alpha. Make all pixels outside the character and weapon fully transparent with alpha 0, including the black vignette, colored halo, glow, shadow, and edge haze; there must be no backdrop of any kind. Keep a clean anti-aliased cutout around the silhouette, with only the alien and complete pistol retained. Do not alter the model, pose, anatomy, clothing, gun size, gun orientation, gun details, or add any object. Do not paint checkerboard squares or any white/black/gray fill. Output a true RGBA transparent PNG suitable as a Meshy reference.
