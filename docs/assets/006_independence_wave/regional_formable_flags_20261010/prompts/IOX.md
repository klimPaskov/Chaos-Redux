# IOX - Indian Ocean League State flag

Route: `mcp__gptimage__generate_image`, quality `high`, size `1600x1008` (the tool returned 1575x999), one call per candidate, no reference image.

## Accepted prompt (candidate 2, `source_png/IOX_imagegen_master.png`)

Fully opaque flat flag graphic, NOT transparent and NOT on a white or black background: the entire canvas from edge to edge is one solid turquoise-blue (rgb 18 98 126) flag field, with no transparency anywhere and no vignette. Original fictional flag of the Indian Ocean League State (two islands joined by a sea lane). One centered emblem only, in three parts: (1) one large and one small island mass in ivory (rgb 240 232 205), bold simple faceted angular silhouettes with straight edges, the large island on the left and the small island on the right, clearly separated; (2) a single gold (rgb 235 188 92) arc band, the sea lane, curving gracefully from the large island over to the small island above the water line; (3) beneath the islands two narrow parallel horizontal wave bands in ivory. Balanced, heraldic, crisp precise edges. The emblem is centered and fills about two-thirds of the canvas height with generous turquoise margins on all sides so the turquoise field is clearly visible around it. Proportion about 82:52 (1.58:1). Solid flat colour fills only, bold shapes that survive shrinking to 10x7 pixels. No sun, no sun disc, no star, no cross, no crescent. No text, letters, numbers, borders, frames, badges, extra symbols, flagpole, fabric, folds, waving, perspective, shadows, gradients, texture, or surrounding scene.

## Rejected candidate 1 (`source_png/IOX_rejected_v1_transparent.png`)

Same concept without the explicit opaque-canvas instruction. The tool returned an RGBA image with a fully transparent field and a washed-out ivory-on-white appearance, with ragged organic island outlines and a sea-lane arc that did not touch either island. Rejected for the missing opaque field and the weak construction. It was not resized or composited.

## Review of the accepted result

Opaque RGB, field about rgb 13 100 130 (specified 18 98 126). One large and one small ivory island, a gold arc rising from the large island to the small one, two ivory wave bands. No sun disc, star, text, or border. The gold arc and two wave bands survive at 41x26, and at 10x7 the two ivory masses with a gold line above and a pale band below remain distinct from the sibling MRX (navy, sun over three islands). Accepted without redrawing.
