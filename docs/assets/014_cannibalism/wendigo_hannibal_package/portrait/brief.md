# Wendigo Hannibal Portrait Animation Brief

- Asset: transformed Wendigo Hannibal portrait
- Event: 014 Cannibalism
- In-game use: revealed leader portrait and post-reveal transformation GUI
- Subject: reveal-gated alternate-history Hannibal Lecter in his transformed supernatural form, without a screen-actor likeness
- Frame size: 156 by 210
- Frame count: 8
- Sheet size: 1248 by 210
- Static fallback: `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`
- Animated sheet: `gfx/leaders/014_cannibalism/hannibal_wendigo_sheet.dds`
- Static sprite: `GFX_portrait_ZZZ_hannibal_wendigo`
- Animated sprite: `GFX_portrait_ZZZ_hannibal_wendigo_animated`
- Animation rate: 4 FPS
- Looping: yes
- Play on show: yes
- Anchor: bottom-center, eyes held in the upper-middle portrait band
- Source mode: eight separate built-in image-generation outputs, with the ordinary fictional face used only as an identity reference and the finished Wendigo super-event source used only as a palette/body-horror reference
- Visual continuity: same face, camera, shoulders, scavenged 1930s military mantle, ruined frozen command room, and cold blue-grey palette in all frames
- Required drawn change: every frame redraws pose or expression, silhouette, frost, blood, exposed flesh, breath, and lighting according to the frame plan
- Prohibited: transforms or filters as motion, antlers, horns, animal skulls, runes, totems, dreamcatchers, headdresses, feathers, beadwork, living-cultural regalia, readable text, real-person likeness
- Reveal gate: the public reveal flag is the only eventual visibility boundary; the asset package does not add a pre-reveal alias or public token
- Target GFX file: `interface/014_cannibalism.gfx` or the current character portrait registry selected by the integration owner
- Target character: `ZZZ_hannibal_wendigo`

The current `hannibal_wendigo.dds` is replaced because the audited source is a flat black silhouette with antler-like imagery and does not preserve the fictional leader's face or meet the cold body-horror contract.
