# Air Winter Visible Climate Asset Prompt

Create the visual asset package for state-based Air Winter and the normal-map climate transformation after the implementation agent proves the supported engine surfaces.

This prompt does not authorize guessing texture dimensions, atlas layout, shader channels, weather entity names, map particle hooks, or mapmode strip slots. The implementation agent must first provide the exact verified target files, sizes, frame ownership, and sprite names.

## Visual promise

The player must see that the world is colder without opening a tooltip.

The presentation has four coordinated layers:

1. dedicated winter mapmode
2. normal-map atmospheric grade
3. region-specific ground and weather cues
4. state or province markers for severe and exceptional conditions

The mapmode is a diagnostic layer. The normal map must carry a visible climate state during ordinary play.

## Visual classes

Prepare a coherent family for these classes:

- boreal and continental
- cool temperate
- Mediterranean and dry temperate
- tropical humid
- tropical seasonal and savanna
- arid and desert
- highland and mountain
- maritime and island
- polar and subpolar

Each class needs phase directions for phase 0 through phase 6. Phase 0 is ordinary baseline. Phase 6 is the most severe persistent cold state.

Do not place universal snow across all classes.

Use the accepted visual matrix for:

- snow depth and persistence
- frost
- cold rain and sleet
- ash cover
- dead or browned vegetation
- frozen rivers, lakes, and coasts where appropriate
- dry dust and failed seasonal rains
- reduced daylight and low-contrast atmosphere
- thaw mud, flood, ice breakup, and damaged vegetation during recovery

## Required assets after engine proof

### Mapmode assets

- one selected mapmode strip frame
- one deselected mapmode strip frame
- winter phase legend
- phase swatches
- hazard markers for food collapse, shelter failure, frozen route, damaged power, thaw flood, and ultraviolet stress where the final GUI uses them
- static tooltip icons where useful

The implementation agent supplies the verified strip frame index and exact strip dimensions. Do not edit the strip before that handoff.

### Atmospheric and map assets

Produce only the asset types the verified engine path can use.

Possible verified outputs may include:

- normal-map color-grade or overlay textures
- weather or particle textures
- ground-state decals
- state or province marker sprites
- frozen-water overlays
- ash and snow blend textures
- dim-daylight or haze layers
- thaw and flood visual states
- static fallbacks for any animated state

Do not create final game assets for a surface that has no proven wiring route.

### Scripted GUI and information assets

- compact winter phase header
- regional visual-class icon set
- adaptation indicator
- active cold-wave warning
- thaw warning
- event or decision category header where required
- static fallback for every animated element

## Animation rules

Use animation only where it communicates state.

Suitable animated candidates:

- severe cold-wave warning pulse
- drifting ash or snow layer
- freeze-to-thaw transition marker
- frozen-route warning
- ultraviolet recovery warning

Follow the frame-animation skill. Every meaningful frame requires its own source art. Provide a static fallback, source frames, processed frames, frame sheet, DDS, preview GIF, contact sheet, manifest, and GFX handoff.

Do not create motion by shifting, scaling, recoloring, blurring, or pulsing one still image.

## Style

The climate package should read at strategic-map scale.

Use:

- broad readable values
- restrained texture
- low visual noise
- clear phase escalation
- regional distinction
- legible severe-state markers
- period-appropriate visual language

Avoid:

- bright fantasy snow
- cinematic blue filters over every state
- modern climate graphics
- readable generated text
- thick glowing borders
- identical treatment for desert, jungle, highland, and boreal states
- visual effects that hide front lines, borders, supply, units, or state selection

## Source mode

Most climate textures, symbols, and fictional map presentation can use generated source art through the correct asset worker.

Use sourced material only when a real historical photograph, flag, person, institution, or attested symbol is required.

The map texture and interface package must remain Fallout and Air Winter owned. Do not reuse zombie, chemical, Death, or unrelated event assets.

## Working folders

Use:

- `docs/assets/air_cleanliness_fallout/winter_climate/`
- `gfx/interface/fallout_world_end/winter_climate/` for Fallout-owned interface assets
- the verified engine-required map or weather folder for normal-map assets
- engine-required mapmode strip roots only after proof

The asset manifest must record every engine exception.

## Deliverables

For every final asset:

- source file
- processed PNG preview
- final DDS or required engine format
- exact dimensions
- source mode
- visual class
- phase or state
- sprite or texture name
- target game path
- target GFX or map definition
- static fallback where relevant
- wiring notes
- status
- uncertainty

Create contact sheets showing:

- all nine visual classes across phases
- mapmode swatches
- normal-map severe-state markers
- animation frames where used
- readability against representative political, terrain, supply, and front-line backgrounds

## Review gates

The package does not pass when:

- the mapmode works but the normal map does not look colder
- all biomes receive the same snow treatment
- the visual state contradicts the mechanical phase
- the map becomes hard to read
- a final asset was produced for an unverified engine surface
- animated assets lack real source frames or static fallbacks
- asset ownership points into another feature folder
