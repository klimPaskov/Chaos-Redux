# CXT flag GFX handoff

- Final normal path: `gfx/flags/CXT.tga`.
- Final medium path: `gfx/flags/medium/CXT.tga`.
- Final small path: `gfx/flags/small/CXT.tga`.
- Sprite name: not applicable; standard HOI4 country flags are resolved by the tag filename `CXT`.
- Target `.gfx`: none for the standard flag consumer.
- Use: fictional Chaos Redux test-country identity flag for tag `CXT`.
- Format: uncompressed 32-bit true-color TGA, descriptor `0x08`, bottom-left origin, exact Vanilla-compatible ladder sizes.
- Review/source package: `docs/assets/country_flags/cxt_test_country/`.

Do not wire the review PNG, contact sheet, or review DDS as runtime flag textures. No custom `.gfx` registration is required unless a later parent-owned GUI introduces a separate explicit sprite consumer.
