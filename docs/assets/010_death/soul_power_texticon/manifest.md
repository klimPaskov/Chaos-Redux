# Death soul power texticon asset manifest

Disposition: implemented and wired; runtime decision-row visual acceptance pending.
Acceptance basis: G5 release repair for a visible custom currency price; stable sprite registered before generation.

The source was generated with native ImageGen transparency and is archived unchanged.
Processing crops unused transparent canvas, scales to fit a centered 18x18 native canvas, and converts the same pixels to uncompressed BGRA32 DDS.
No reference artwork is shipped as this icon.
The parent reviewed the supplied small contact sheet, native glyph and nearest-neighbor enlargement on a dark field.
The symbol remains recognizable, corners are transparent, and decoded DDS pixels match the processed PNG exactly.

## Runtime handoff

- Sprite: `GFX_death_soul_power_texticon` in `interface/010_death.gfx`, a one-frame `spriteType`.
- Texture: `gfx/interface/texticons/010_death/010_death_soul_power_texticon.dds`.
- Source: `source/010_death_soul_power_imagegen_source.png`; processed PNG: `processed/010_death_soul_power_texticon.png`.
- Source canvas: 1254x1254; output: 18x18; alpha range (0, 255); transparent pixels 184.
- Exact content hashes and native alpha checks: `manifest.json`.

## Limits

The full decision-panel row has not been successfully rendered by MCP or checked in game.
The archived references are inspection evidence only.
The specialist capacity failure also prevented its Soul glyph handoff; the parent completed the pre-authorized native ImageGen request and reviewed the 760x470 contact sheet.
The source prompt is `prompt.txt`; no background-removal fallback was needed.
