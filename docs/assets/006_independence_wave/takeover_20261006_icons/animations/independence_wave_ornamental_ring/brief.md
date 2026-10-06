# Event 006 ornamental bronze ring overlay

In-game use: shared decorative overlay for the Event 006 status-panel seals while optional animation is enabled.

Consumer: parent-owned repoint of the four existing status frameAnimatedSpriteType entries in interface/006_independence_wave.gfx to one shared decorative loop. The overlay frame has a transparent centre so it does not obscure the current recognition, dependency, charter, or formable state icon.

Target: eight independently authored 64x64 transparent frames assembled left-to-right into a 512x64 horizontal sheet. Anchor: canvas centre (32,32), fixed outer-rim centre and diameter, at least 2px clear outer margin, broad transparent centre aperture; the final frames keep a 36px diameter zero-alpha circle, with an approximately 41px minimum alpha>=16 inner gap.

Motion: one small ink-and-bronze ribbon flourish traces clockwise around the rim over eight real ImageGen frames. The bronze rim itself stays visually stable; each frame is a distinct generated source state for the flourish, with no script-created motion or transform-only frame.

Timing: 5 FPS (200 ms per frame), looping, play-on-show. Static fallback: frame 000. The sheet is not a semantic status indicator. The prompt requested a 48px aperture; the accepted native-alpha frames measured approximately 41px at alpha>=16 while retaining the fully transparent 36px center required to leave the underlying symbol visible.

Background mode: native transparent for every generated frame; centre aperture and unused canvas remain transparent. Background removal is not used.

Sources and prompts are retained in source_frames/ and prompts/. Processed frames, sheet, static fallback, GIF and contact sheet are retained in their named subfolders.
