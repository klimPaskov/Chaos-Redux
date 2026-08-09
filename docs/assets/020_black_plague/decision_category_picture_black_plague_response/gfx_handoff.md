# GFX handoff — Event 020 Black Plague decision category picture

Asset status: `complete`; runtime registration is wired.

- Sprite name: `GFX_decision_cat_picture_black_plague_response`
- Final DDS: `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`
- Native canvas: `114x101`, one static frame, opaque RGBA/BGRA (`alpha 255..255`)
- Decision category consumer: dedicated Black Plague response/cure category (`common/decisions/categories/020_black_plague_response_categories.txt`)
- Registered `.gfx`: `interface/020_black_plague_response.gfx`

Registered sprite definition:

```text
spriteType = {
	name = "GFX_decision_cat_picture_black_plague_response"
	texturefile = "gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds"
	noOfFrames = 1
}
```

`interface/020_black_plague_response.gfx` registers the sprite and `common/decisions/categories/020_black_plague_response_categories.txt` consumes it. The generated source, exact prompt, processed PNG, DDS, contact sheet, and header/round-trip QA remain in [`docs/assets/020_black_plague/decision_category_picture_black_plague_response/`](../../../../assets/020_black_plague/decision_category_picture_black_plague_response/). No placeholder or fallback was used.
