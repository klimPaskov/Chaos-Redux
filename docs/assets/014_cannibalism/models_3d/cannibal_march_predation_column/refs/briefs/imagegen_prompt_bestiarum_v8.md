# Bestiarum Fleshmad Hunter v8 ImageGen prompt

## Approved source

- Source: Bestiarum Games, *Fleshmad Hunters | Man Eaters — Hunter 1*
- Source page: https://bestiarumgames.com/products/flesh-hunters-man-eaters-bestiarum-miniatures-d-d-wargaming-dnd
- Direct source image: https://bestiarumgames.com/cdn/shop/files/07_FleshmadHunter1.jpg?v=1749571234&width=1080
- Source SHA-256: `9E0028B6458CFD4876D347A44EEBD0FB4B533DDF71F10ABA6B73E42D3F0F668F`
- Source mode: `reference_only_user_authorized`

## Material-interpretation prompt

Faithful cleanup-only material interpretation of the supplied official Bestiarum Fleshmad Hunter 1 tabletop render for a single-character 3D-model reference. Preserve EXACTLY the same adult human anatomy, fierce face, running pose, limb positions, proportions, silhouette, bone-spike crown/headgear, skull breast trophy, feather/fur mantle, crude wraps and clothing, bone greatbow shape and hand placement, barbed arrow/shaft in the other hand, back quiver and every existing piece of gear. Do not add, remove, replace, resize, relocate, stylize, modernize, armor, knightify, or redesign anything. Remove only the round display base, black studio background, red rim-light presentation, dust, and cast shadow. Render the exact existing character in restrained realistic full color: weathered human skin, dark scavenged hide and cloth, aged ivory bone and skull, dark natural feathers/fur, rough brown wood/cord/sinew, dirty iron only where the source already has metal. Add conspicuous but culturally neutral horror body and face paint using irregular smeared ash-white and dried dark-red streaks/blotches with no symbols, no geometry, no sacred or living-community motifs. Keep the source's grim horror identity and source-matched detail. One isolated full-body subject centered with all gear and extremities fully visible, no crop, no ground plane, no pedestal, no scenery, no text, no extra figures, no extra weapons. Genuine transparent RGBA background and transparent unused canvas, clean antialiased edges, no checkerboard, no white or colored matte, no halo, no internal alpha holes.

## Transparency-repair prompt

Transparency repair only. Preserve every visible character pixel, color, material, paint mark, anatomy, face, running pose, proportions, silhouette, bone-spike crown, skull breast trophy, feather/fur mantle, clothing, wraps, bone greatbow, barbed arrow, quiver and gear exactly as supplied. Do not redraw, restyle, recolor, crop, move, add, remove or redesign anything. Remove only the baked gray-and-white checkerboard background and any background matte. Output genuine transparent RGBA unused canvas with clean antialiased alpha edges, no checker pattern, no backdrop, no pedestal, no ground, no cast shadow, no halo, no internal alpha holes. Keep the full subject and every extremity fully inside the canvas.

## Route result

The material interpretation preserved the approved identity but returned a baked checkerboard in a 24-bit RGB PNG. The targeted transparency repair returned a new opaque studio backdrop and was rejected. The approved final therefore uses the first material interpretation with the documented local rembg 2.0.61 background-removal fallback, boundary-only checker decontamination, and a narrow antialiased edge.

The exact approved final is `refs/original/meshy_input.png`, SHA-256 `74253F5B89DB675D39F94AF7007358116FB21F30BAA0CF85572580FAC5308D10`.
