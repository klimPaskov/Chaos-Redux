# Air Winter Regional Visual Generation Prompts

These are the retained generation briefs for the six fictional source plates used by this package. All requested imagery is original game-asset material with no logos, text, flags, characters, real locations, or borrowed game assets.

## Boreal continental material detail

> Create a seamless square game-material texture for a fictional post-nuclear Air Winter ordinary-map overlay in a boreal continental region. Top-down orthographic material study only: dark frozen conifer soil, granular frost, thin irregular snow crust, cold blue-grey earth, sparse black organic debris, subtle rail-side grit, and fine ice crystals. Natural random distribution, no horizon, no objects larger than texture detail, no buildings, no people, no text, no borders, no icons. Physically readable diffuse color with strong fine surface detail suitable for deriving a normal map and specular map. Avoid pure white snow, avoid green radiation colors, avoid zombie imagery. Tileable edges, evenly lit, realistic strategy-game texture, 1:1 square.

Output source: `source_png/materials/boreal_continental_detail_source.png`.

## Nine-class regional material atlas

> Create one square 3x3 atlas of nine clearly separated top-down seamless material studies for a fictional Hearts of Iron-style Air Winter ordinary-map asset package. Use equal cells, consistent neutral overhead lighting, and realistic game texture detail. Include no labels, text, perspective horizon, buildings, people, flags, UI, or recognizable landmarks. Cell order left-to-right, top-to-bottom: 1) boreal continental frozen dark soil with conifer litter and frost, 2) temperate maritime wet grey earth with sleet and moss, 3) Mediterranean pale agricultural soil with orchard frost and dry grass, 4) desert and arid plateau ochre stone with cold dust and frost around cracks but no blanket snow, 5) tropical coast and monsoon dark wet ground with weakened leaf litter and cold rain, 6) equatorial rainforest black wet earth with chilled mist residue, ash caught in vegetation, and canopy litter, 7) mountain highland exposed rock with deep frost and wind-packed snow, 8) island oceanic salt-dark stone, wet turf, cold spray, and sparse frost, 9) polar subpolar blue-black ice, compact snow, and dark grit. Preserve regional identity. Warm regions must look colder without turning universally white. Fine physical detail suitable for diffuse, normal, and specular derivation. 1:1 square.

Output source: `source_png/materials/regional_material_atlas_source.png`.

## Four-family particle frame atlas

> Create a square 4x4 particle-frame atlas on a pure black background for a fictional post-nuclear Air Winter strategy-game map. Use sixteen equal cells with no grid lines, text, labels, scenery, horizon, or UI. Each cell contains a different independently drawn particle arrangement centered with generous empty black space. Frames must change their internal shapes and clusters, not merely move or rotate the same drawing. Rows left-to-right: Row 1 snow and frost - four distinct states of pale blue-white flakes, frost crystals, ice needles, and wind-torn clusters. Row 2 cold rain and mist - four distinct states of slate-blue droplets, sleet streaks, beads, and low fog wisps. Row 3 ash and dirty snow - four distinct states of charcoal ash fragments, soot specks, grey contaminated snow clumps, growing from sparse to terminal density. Row 4 thaw and flood - four distinct states of wet slate droplets, splash crowns, muddy ripples, melt fragments, and runoff arcs. Crisp alpha-friendly silhouettes, soft detail only inside particles, no radiation green, no fire, no zombies. High-contrast VFX source art, 1:1 square.

Output source: `source_png/particles/regional_particle_frames_source.png`.

## Nine-class dead vegetation atlas

> Create one square 3x3 atlas of fictional dead-vegetation cutout source art on pure black backgrounds, equal cells, no labels, no text, no grid lines, no scenery, no horizon. Top-down to shallow-oblique isolated clusters suitable for transparent strategic-map ground cards. Cell order left-to-right, top-to-bottom: boreal continental blackened conifer scrub, temperate maritime collapsed wet hedges and brown grass, Mediterranean frost-killed orchard branches and pale vines, desert arid plateau dead thorn scrub and dry reeds, tropical coast monsoon wilted broad leaves and broken palms, equatorial rainforest dark canopy litter, dead lianas, and wet ash-coated leaves, mountain highland frozen alpine scrub, island oceanic salt-burned low vegetation, polar subpolar sparse buried tundra stems. Every cell must have a distinct silhouette and regional botany while remaining fictional and non-identifiable. Cold grey-brown palette, alpha-friendly against black, no people, buildings, flags, logos, text, fire, radiation glow, or zombie imagery. 1:1 square.

Output source: `source_png/props/dead_vegetation_atlas_source.png`.

## Nine-class frozen-water atlas

> Create one square 3x3 atlas of fictional frozen-water and ice-edge cutout source art on pure black backgrounds, equal cells, no labels, no text, no grid lines, no complete landscapes or horizons. Top-down isolated irregular patches suitable for transparent strategy-map overlays. Cell order left-to-right, top-to-bottom: boreal river ice with white fractures, temperate maritime slushy harbour-edge ice and dark water, Mediterranean thin valley frost-ice with exposed dark channels, desert arid plateau frozen well and pipeline seep with cracked mineral rim but not a snow field, tropical coast monsoon rare cold highland water glaze with rain-dark edges, equatorial rainforest dark river skin ice only as extreme anomaly with wet vegetation fragments, mountain highland thick blue glacier-fed ice with cracks, island oceanic salt-grey harbour glaze and rough-water edge, polar subpolar heavy blue-black sea ice with pressure fractures. Distinct silhouettes, realistic cold blue-grey materials, alpha-friendly against black, no ships, people, buildings, flags, icons, text, radiation green, or zombie imagery. 1:1 square.

Output source: `source_png/props/frozen_water_atlas_source.png`.

## Six-phase atmospheric grade atlas

> Create one square 3x2 atlas of six abstract fictional Air Winter atmospheric grade textures, equal cells, no labels, no text, no grid lines, no scenery, no objects, no horizon. These are subtle full-screen color-grade alpha sources for a grand-strategy ordinary map. Left-to-right, top-to-bottom: Phase 1 thin cold blue-grey haze with very light soot grain, Phase 2 clearer cold desaturation and low cloud texture, Phase 3 darker infrastructure-winter blue-grey with restrained fog, Phase 4 black-harvest charcoal haze and visibly dimmed noon light, Phase 5 heavy ash-winter slate/soot veil with lower contrast, Phase 6 terminal cold near-black blue-grey atmospheric grain, strongest but still transparent enough for map readability. Use soft irregular cloud/soot variation across each entire cell, no hard vignettes, no pure opaque black, no radiation green, no fire, no UI, no symbols. Consistent texture scale, seamless-feeling edges, 1:1 square.

Output source: `source_png/grades/phase_grade_atlas_source.png`.

## Processing note

The source plates were not used directly as final game files. `_tooling/process_regional_visuals.py` crops and normalizes them, derives alpha/normal/specular channels, applies the approved class/phase art-direction values, generates review surfaces, and performs explicit DirectXTex DDS conversion. Source SHA-256 values are recorded in `build_report.json`.
