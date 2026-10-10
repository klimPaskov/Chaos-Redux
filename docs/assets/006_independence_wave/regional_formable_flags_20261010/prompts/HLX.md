# HLX - Horn League State flag

Route: `mcp__gptimage__generate_image`, quality `high`, size `1600x1008` (the tool returned 1575x999), one call per candidate, no reference image.

## Accepted prompt (candidate 2, `source_png/HLX_imagegen_master.png`)

Fully opaque flat flag graphic, NOT transparent and NOT on a white or black background: the entire canvas from edge to edge is one solid terracotta red-brown (rgb 142 64 40) flag field, with no transparency anywhere and no vignette. Original fictional flag of the Horn League State (a league of highland and coast). One centered emblem only, in three stacked parts: (1) a stepped angular plateau of three tiers in ivory (rgb 240 232 205), a symmetrical stair-step silhouette with a flat top and three clearly separated tiers; (2) beneath it a single curved coastline arc band in sand colour (rgb 232 198 120), a gentle concave sweep; (3) beneath the arc a small neat horizontal row of five round well-dots in sand colour. Symmetrical, balanced, heraldic, crisp precise edges. The emblem is centered and fills about two-thirds of the canvas height with generous terracotta margins on all sides so the terracotta field is clearly visible around it. Proportion about 82:52 (1.58:1). Solid flat colour fills only, bold shapes that survive shrinking to 10x7 pixels. Absolutely no cross, no crescent, no star, no lion, no religious or royal glyph. No text, letters, numbers, borders, frames, badges, extra symbols, flagpole, fabric, folds, waving, perspective, shadows, gradients, texture, or surrounding scene.

## Rejected candidate 1 (`source_png/HLX_rejected_v1_transparent.png`)

Same concept without the explicit opaque-canvas instruction. The tool returned an RGBA image with a transparent, dark-fringed field and a ragged brown halo around the emblem instead of a flat full-bleed field. Rejected for violating the flat opaque field and clean-edge constraints. It was not resized or composited.

## Review of the accepted result

Opaque RGB, field about rgb 135 65 42 (specified 142 64 40). Centered emblem: three-tier ivory plateau, one sand coastline arc, a row of five sand well-dots. No cross, crescent, star, lion, solomonic or religious glyph, and no lettering. The plateau steps and the dot row stay readable at 41x26, and at 10x7 the ivory stepped block over a sand line is the distinct read. Accepted without redrawing.
