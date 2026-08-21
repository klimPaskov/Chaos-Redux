# CXT flag GFX handoff

- Final normal path: `gfx/flags/CXT.tga`.
- Final medium path: `gfx/flags/medium/CXT.tga`.
- Final small path: `gfx/flags/small/CXT.tga`.
- Sprite name: not applicable; standard HOI4 country flags are resolved by the tag filename `CXT`.
- Target `.gfx`: none for the standard flag consumer.
- Use: fictional Chaos Redux test-country identity flag for tag `CXT`.
- Format: uncompressed 32-bit true-color TGA, descriptor `0x08`, bottom-left origin, exact Vanilla-compatible ladder sizes.
- Processed/runtime colour contract: exactly four hard RGB colours — charcoal `(31,32,35)`, toxic chartreuse `(184,224,4)`, white `(255,255,255)`, and crimson `(207,20,53)` — with no gradient or vignette.
- Small-size note: `gfx/flags/small/CXT.tga` uses the documented manual 10×7 simplification and retains the white reticle/diamond plus crimson warning pixels.
- Review/source package: `docs/assets/country_flags/cxt_test_country/`.

Do not wire the review PNG, contact sheet, or review DDS as runtime flag textures. No custom `.gfx` registration is required unless a later parent-owned GUI introduces a separate explicit sprite consumer.
