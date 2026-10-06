# Broken-chain spirit icon source record

## Initial built-in ImageGen prompt

Use case: stylized-concept.
Asset type: Hearts of Iron IV national-spirit icon, processed to an exact transparent 60x68 canvas.
Primary request: Create one original Soviet nuclear-deterrence medal badge showing a dark olive-steel atomic warhead centered upright, with one heavy broken chain draped across the warhead and its two snapped ends clearly visible at the front. Place the warhead and chain inside a compact red-and-black Soviet military medal composition.
Style/medium: richly painted mid-century Soviet medal art matching a grim, bronze-highlighted historical strategy-game icon set. Use dark blackened steel, deep crimson red enamel, aged brass edging, restrained gold-bronze highlights, and a few muted olive metal surfaces. The medal frame should feel stamped and engraved, with a compact laurel or ribbon detail and one small red star accent; keep those ornaments subordinate to the warhead and broken chain.
Composition/framing: centered and vertically balanced, readable at tiny 60x68 size; make the complete badge silhouette fill about 88% of canvas height and width while leaving a narrow safe margin. Keep every medal edge, laurel tip, chain link, and warhead tip fully inside the canvas. The red-and-black medal face belongs inside the badge artwork; only the space outside the badge silhouette is transparent.
Background: genuine transparent alpha in the initial output around the medal silhouette, with no outer square or scene.
Avoid: loose pile of chain, papers, workshop scene, landscape, people, flags, large Soviet emblems, text, letters, numbers, watermark, generic round coin without a badge silhouette, pale white border, achievement frame, square tile, opaque canvas background, fake checkerboard, chroma background, matte pixels, fringe, broad halo, clipped edges, unintended holes.

## Background-only edit prompt

Use case: background-extraction.
Input image: Image 1 is the accepted nuclear medal badge and is the edit target.
Primary request: Change only the checkerboard outside the badge silhouette to genuine transparent alpha. Preserve the central dark olive warhead, the snapped chain links, the red-and-black Soviet medal field, bronze rim, laurel, red star, exact colors, internal opacity, crop, lighting, framing, and every edge detail.
Keep the whole badge intact. Do not repaint, redraw, blur, sharpen, move, resize, warp, recolour or add any element. Remove only background checkerboard pixels outside the complete medal silhouette. Preserve a clean antialiased edge with no grey checker spill or matte fringe. Keep the medal face itself fully painted and opaque.
Output a PNG with real transparent unused canvas around the badge. Do not leave or replace the checkerboard with another backdrop.

## Generation trace

Built-in `image_gen.imagegen` generated the initial source at `C:/Users/klimp/.codex/generated_images/01a10fb8-9773-7252-b990-c8265513a127/exec-85262505-c34d-4bf7-9f1f-4e6066545dc4.png`. The initial output was opaque with a checkerboard; the untouched copy is `source_png/imagegen_initial/sov_nuclear_spirit_broken_chain_initial.png`.

Built-in `image_gen.imagegen` then performed the background-only edit using that generated file as its sole edit target and `transparent_background=true`. The selected source is `source_png/transparent_edit/sov_nuclear_spirit_broken_chain_background_edit.png`; its untouched generated output path was `C:/Users/klimp/.codex/generated_images/01a10fb8-9773-7252-b990-c8265513a127/exec-603fd904-4d7c-42ea-a473-66ca0d36eeae.png`.
