# LKX - Great Lakes Federation flag

Route: `mcp__gptimage__generate_image`, quality `high`, size `1600x1008` (the tool returned 1575x999), one call per candidate, no reference image.

## Accepted prompt (candidate 2, `source_png/LKX_imagegen_master.png`)

Fully opaque flat flag graphic, NOT transparent and NOT on a white background: the entire canvas from edge to edge is one solid deep green (rgb 58 112 58) flag field, with no transparency anywhere. Original fictional flag of the Great Lakes Federation (three lakeshore kingdoms). One centered emblem only: three layered ivory (rgb 240 232 205) lake-ripple arcs, each a bold uniform-width curved band with clear green gaps between them, stacked concentrically like a stepped fan and ending in angular squared-off tips, resting beneath one small ochre (rgb 232 196 96) angular hill or peak triangle that sits above the top arc. Symmetrical, balanced, heraldic, crisp precise edges. The emblem is centered and fills about two-thirds of the canvas height with generous green margins on all sides, so the green field is clearly visible around it. Proportion about 82:52 (1.58:1). Solid flat colour fills only, bold shapes that survive shrinking to 10x7 pixels. No text, letters, numbers, stars, suns, crosses, crescents, animals, borders, frames, badges, extra symbols, flagpole, fabric, folds, waving, perspective, shadows, gradients, vignettes, texture, or surrounding scene.

## Rejected candidate 1 (`source_png/LKX_rejected_v1_transparent.png`)

Same concept with the field colour described but without the explicit opaque-canvas instruction. The tool returned an RGBA image whose field was transparent, leaving only the fan emblem on an alpha background, so the flat full-bleed field constraint failed. The prompt added "no gradients, vignettes" but did not forbid transparency. It was not resized or composited.

## Review of the accepted result

Opaque RGB, field about rgb 63 113 61 (specified 58 112 58), one centered emblem: three ivory concentric ripple bands under a small ochre peak. No text, border, gradient or shadow. The three arcs stay separated at 82x52 and 41x26, and the ochre peak over the ivory fan remains the distinct read at 10x7. Accepted without redrawing.
