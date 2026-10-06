# Shared achievement medallion/laurel ImageGen lineage

All calls used the built-in ImageGen tool with native transparent background enabled. Source images were retained separately from processed and final assets.

## Candidate 1

Tool output: C:/Users/klimp/.codex/generated_images/01a10fb8-b1a2-77c1-8af2-985345bab0a1/exec-7add0022-9b1a-4be3-995d-db1464a75953.png
Retained source: docs/assets/024_video_game_in_sweden/source_png/repairs_20261006/achievement_shared_medallion_laurel_candidate1.png
Disposition: rejected because outer leaves touched the canvas and were clipped.

Prompt:
Use case: original foreground artwork for a Hearts of Iron IV achievement icon.
Create one original painted emblem on a square canvas: a front-facing, circular, dark gunmetal and aged-bronze campaign medallion with a symmetrical laurel wreath wrapping the outside rim. Match the subdued charcoal metal, brass edge highlights, textured shading, and crisp readable leaf silhouette seen in Chaos Warfare achievement medals. This is one shared foreground frame for two separate achievement symbols; do not add any central picture or symbol.
Composition: the complete medallion and wreath are centered, nearly 60 pixels wide when reduced to 64x64, with a 2-3 pixel clear margin. Keep the central circular enamel face completely empty and genuinely transparent so separate generated achievement art can show through it. The entire area outside the metal and leaves must also be genuinely transparent. Use real alpha, not a checkerboard or painted dark backdrop.
Style: aged hand-painted strategy-game metal, clear dark outline, restrained brass glints, saturated enough to remain distinct on the standard dark achievement card at 64x64. Front view, clean symmetrical silhouette, no clipped leaves, no broad shadow or glow.
Constraints: no square card, no outer UI frame, no ribbon, no text, no letters, no numbers, no flag, no face, no skull, no compass, no map, no red cross, no watermark, and no extra objects.

## Candidate 2 edit

Tool output: C:/Users/klimp/.codex/generated_images/01a10fb8-b1a2-77c1-8af2-985345bab0a1/exec-cd51ad24-fb41-428b-bd2f-b80b5ec96256.png
Edit target: docs/assets/024_video_game_in_sweden/source_png/repairs_20261006/achievement_shared_medallion_laurel_candidate1.png
Retained source: docs/assets/024_video_game_in_sweden/source_png/repairs_20261006/achievement_shared_medallion_laurel_candidate2.png
Disposition: selected shared frame source. It has complete leaves and a transparent center; isolated alpha-1 bottom-edge residue was removed by the documented one-pixel local defringe pass.

Prompt:
Edit image 1, which is the original shared achievement medallion foreground. Make one composition correction only: restore the complete missing outer laurel-leaf tips and metal rim, especially at the bottom and left/right edges, and scale/recenter the complete emblem so the whole silhouette has at least a 5% genuinely transparent margin on every side of the square canvas. Keep the same dark gunmetal and aged-bronze finish, hand-painted strategy-game style, frontal symmetry, ring thickness, leaf pattern, and overall proportions. Keep the entire circular inner opening truly transparent for separate symbol art. Preserve real alpha outside the emblem and through the opening. Do not add any central content, square background, shadow, glow, ribbon, text, letters, numbers, flag, UI frame, or new objects.
