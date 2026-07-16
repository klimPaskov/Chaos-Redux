# Event 012 Africa Focus-Family Icon Prompt Record

## Production record

- Production date: 2026-07-17
- Source mode: generated original artwork through the built-in OpenAI image generation tool
- Use case: static Hearts of Iron IV national-focus icons
- Final canvas: 94 x 86 pixels with a transparent background
- Generation method: one independent generation per icon; no source image was reused as another icon's master
- Chroma workflow: flat `#ff00ff` generation background, followed by soft matte removal and despill

The files in `../source_png/` are the unchanged high-resolution PNGs returned by the generation tool. They are retained as the provenance-bearing source masters. The files in `../alpha_png/`, `../processed_png/`, and the final DDS folder are derivatives.

## Shared prompt contract

Every generation used the following art-direction contract together with the asset-specific direction below:

> A single, self-contained grand-strategy national-focus emblem in a painterly 1930s-1940s style. Use aged metal, paper, dark wood, blackened bronze, muted gold, deep green, restrained red, indigo, and ochre. Build one centered, compact silhouette with bold value separation, a dark outer contour, and details that remain legible at 94 x 86 pixels. Isolate the emblem on a perfectly flat, uniform `#ff00ff` chroma-key background with no floor, cast background shadow, border, frame, vignette, glow, text, letters, numbers, watermark, or UI chrome. Do not use real flags, real political emblems, colonial insignia, readable documents, copied game icons, tribal-mask shorthand, animal or safari motifs, pseudo-sacred symbols, ethnic caricature, or a generic Africa silhouette as the whole composition. Treat public institutions, soldiers, workers, and relief work seriously and with dignity.

## Asset-specific directions

### `GFX_goal_africa_focus_family_host_proclamation`

A sturdy period public lectern with two compact microphones, an opened blank charter scroll, a small civic rising-sun seal, and a restrained laurel. The emblem represents a government publicly proclaiming a common continental mandate. It must read as a public act, not as a cult of personality or a real regime.

### `GFX_goal_africa_focus_family_host_legitimacy`

An empty civic council chair behind a sealed ballot box and an upright blank mandate document, framed by a bronze institutional arch and a subdued rising sun. The emblem represents government, coalition, and public consent. Avoid a throne, personal portrait, or leader worship.

### `GFX_goal_africa_focus_family_charter_law`

An open blank constitutional charter on a carved dark-wood reading stand, with a prominent wax seal, balanced bronze scales, and linked legal tablets. The emblem represents binding charter law, courts, and enforceable institutions. Include no readable writing.

### `GFX_goal_africa_focus_family_continental_representation`

A dignified semicircular congress chamber viewed slightly from above, with equal empty seats around a central speaking stand and a ring of small regional civic medallions. The emblem represents equal continental representation. Avoid a throne, flags, people, or territorial borders.

### `GFX_goal_africa_focus_family_protection_guarantee`

Two equal shields interlocked around a blank sealed guarantee charter, secured by a heavy clasp and enclosed by a modest olive wreath. The emblem represents a reciprocal protection guarantee rather than conquest, annexation, or one party shielding a subordinate.

### `GFX_goal_africa_focus_family_volunteer_intervention`

A dignified dark-skinned volunteer's rolled field sleeve and plain white service armband, one hand gripping a medical satchel strap, with a plain period rifle, canteen, and partner shield behind it. Balance military service and humanitarian support. Avoid raised-fist propaganda, uniforms tied to a real regime, and real medical or political emblems.

### `GFX_goal_africa_focus_family_aid_and_relief`

A durable relief crate holding grain, a water canteen, a medical satchel, and clean bandages, supported by bronze helping hands and a protective wreath. The emblem represents organized food, water, and medical relief. Do not use a Red Cross or other protected real-world emblem.

### `GFX_goal_africa_focus_family_regional_congress`

A round congress table viewed from above, surrounded by nine equal empty carved seats and nine blank folios, with a central speaking staff or gavel and an outer linked ring. The emblem represents negotiated regional congress. Include no map, people, or dominant seat.

### `GFX_goal_africa_focus_family_road_corridor`

A broad paved road and steel bridge running toward two equal customs gates, with a survey compass and transport wheel as secondary motifs. The emblem represents a cross-border civil road corridor. Avoid directional arrows, maps, conquest imagery, and readable signs.

### `GFX_goal_africa_focus_family_rail_corridor`

A compact period steam locomotive crossing a rail bridge, with converging rails, a signal lamp, and track fasteners. The emblem represents a shared civil rail corridor and interoperable infrastructure, not military expansion.

### `GFX_goal_africa_focus_family_army_common_reserve`

Three plain period helmets, a sealed supply crate, a transport wheel, and crossed unmarked rifles behind a central shield. The emblem represents shared manpower, equipment, and transport reserves. Include no rank, flag, national badge, or real military insignia.

### `GFX_goal_africa_focus_family_resource_sovereignty`

A locked public resource treasury containing copper ore, an oil-valve wheel, grain, and a gear beneath a civic seal and balanced public-revenue scales. The emblem represents public resource governance and accountable revenue. Avoid foreign-company branding, private treasure, flags, or extraction triumphalism.

### `GFX_goal_africa_focus_family_rival_bloc`

Two equal opposing coalition shields across a broken treaty ring, each backed by a different cluster of linked regional tokens, with a snapped clasp and diverging laurel. The emblem represents rival continental blocs and institutional division. Avoid national flags, territorial maps, ethnic symbols, and battle-glory imagery.

## Reference and rights record

Vanilla focus-icon contact sheets were inspected only to calibrate silhouette density, aging, and small-size readability. No vanilla or third-party artwork was copied, traced, edited, or shipped in this package. All 13 source masters are newly generated originals, so there are no external source URLs, creator credits, or third-party license conditions to carry into the mod.
