# Buddha Mandate Portrait Source Prompts

Generation mode: `$imagegen`, eight individual key-state portrait renders expanded into sixteen playback source-frame files by mirrored ordering.

Input image: `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_png/portrait_THR_godly_figure_reference.png`, converted from `gfx/leaders/THR/portrait_THR_godly_figure.dds` and used as the identity/edit anchor.

Shared individual-frame prompt stem:

> Use the provided reference image as the identity anchor: the same compact orange masked Holy Realm godly figure, large eyes, jeweled crown, ornate side ornaments, front-facing sacred portrait, sun/moon discs. Create one complete portrait frame for the Buddha Mandate animated portrait. Preserve the mask-like face, crown silhouette, centered portrait crop, and sacred icon-painting structure. No labels, text, UI, watermark, simple filter, vignette, hue shift, zoom, warp, or glow-only pulse. The change must be a real drawn key state: subtle mandala halo breathing, crown jewel glints, robe highlights, eye-light variation, and lamp/disc reflections. Keep the image high contrast and readable at 156x210.

Playback order: key states 000-007, then mirrored key states 006-000 with frame 000 held for one extra frame at the loop seam.

| Frame | Prompt emphasis |
| --- | --- |
| 000 | Resting radiance; low halo, subdued crown jewels. |
| 001 | First breath; slightly brighter crown-side halo. |
| 002 | Lamp reflection; warmer cheek and robe highlights. |
| 003 | Crown shimmer; restrained glints on crown ornaments. |
| 004 | Forehead jewel; controlled light at the center jewel. |
| 005 | Mandala intake; denser halo texture behind crown. |
| 006 | Eye glint; subtle eyelid and eye-light change. |
| 007 | Golden crest; halo reaches a restrained crest. |
| 008 | Mirrored key 006; descent from eye glint. |
| 009 | Mirrored key 005; mandala texture lowers. |
| 010 | Mirrored key 004; forehead jewel remains controlled. |
| 011 | Mirrored key 003; crown glints recede. |
| 012 | Mirrored key 002; lamp reflection lowers. |
| 013 | Mirrored key 001; first-breath glow returns near rest. |
| 014 | Mirrored key 000; resting radiance. |
| 015 | Held key 000; rest hold for the loop seam. |
