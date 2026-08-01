# Event 020 super-event 087 generated-art handoff

The optional Rat King global defeat aftermath image is complete and promoted in the parent-owned sprite definition. The resolver remains runtime-gated; live consumer validation is still outstanding.

## Runtime handoff

| Sprite | Final DDS | Target `.gfx` | Size | Use |
| --- | --- | --- | --- | --- |
| `GFX_super_event_087_rat_king_defeat_aftermath` | `gfx/super_events/020_black_plague/super_event_087_rat_king_defeat_aftermath.dds` | `interface/020_black_plague_super_events.gfx` | 457x328 | Super-event ID 87, qualifying long/global defeat aftermath only |

Promoted definition evidence:

```text
spriteType = { name = "GFX_super_event_087_rat_king_defeat_aftermath" texturefile = "gfx/super_events/020_black_plague/super_event_087_rat_king_defeat_aftermath.dds" }
```

## Source and review evidence

- Source mode: official built-in image generation, generated fictional/alternate-history scene.
- Prompt: `docs/assets/020_black_plague/prompts/super_event_087_rat_king_defeat_aftermath_prompt.md`.
- Source PNG: `docs/assets/020_black_plague/super_event_art/source_png/super_event_087_rat_king_defeat_aftermath_source.png` (1479x1063 RGB, SHA-256 `142027431ef030cffd3073ed5968be3c5ea8e070aadf13c495be86aaa188402e`).
- Processed PNG: `docs/assets/020_black_plague/super_event_art/processed_png/super_event_087_rat_king_defeat_aftermath.png` (457x328 RGB, SHA-256 `f0909708b26a6047507756c457a828a308fd1cdf20c82dcf52bc36c3b69ad95e`).
- Contact sheet: `docs/assets/020_black_plague/super_event_art/contact_sheet.png` (review only).
- DDS: SHA-256 `cf7e5f8b21c6a88d26f9700b4232770469c34572d98789054e3b593b5508cbb5`, exact 599,712-byte one-level BGRA legacy header, declared 457x328, pixel-format flags 65, BGRA masks, texture caps `0x1000`, alpha range 255-255.
- Canonical references inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event/contact_sheet.png` and its super-event catalog rows, plus existing Event 020 source/processed images 085 and 086.

## Visual fit and boundary

The image is a solemn dawn reconstruction scene: a ruined industrial city, rebuilding workers, a sealed black crown relic and broken throne behind an iron quarantine gate, and sentries keeping watch. It avoids a clean reset or triumph. The two-tag boundary is preserved visually without text: an ochre civic pennant for `RTA` and the chained black crown seal for defeated `RTX`. No 3D model work was performed. `interface/020_black_plague_super_events.gfx` now registers the stable sprite; the parent still owns final runtime validation and any GUI/consumer checks.

## Remaining uncertainty

The stable sprite name is now registered as `GFX_super_event_087_rat_king_defeat_aftermath`. Retain it unless an existing registry contract requires a documented rename.
