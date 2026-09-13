# Asset and Animation Specification

## Asset strategy

Event 51 needs a coherent documentary visual package. The main subjects should be people, infrastructure, water, agriculture, troops, and damaged land. Maps can appear as secondary props but should not dominate the event art.

The asset inventory below is the complete authorized Event 51 package.

## Source modes

### Generated documentary art

Use native ImageGen for fictional or composite period-authentic scenes that do not need to depict a specific real event or person.

The images should resemble 1936 to 1945 documentary photography or period news photography. Avoid modern cooling towers, modern emergency vehicles, plastic water tanks, contemporary uniforms, electronic displays, modern road markings, and readable generated text.

### Sourced archival art

Use archival sources when a picture must represent a real historical heat wave, location, military campaign, rail practice, or documented public response. Record source, archive, date, rights, and why it fits.

### Icons

Use native transparent ImageGen through the icon workflow. Preserve true alpha, use one clear subject, and design separately for each icon type.

## Runtime placement pattern

Final event-owned assets should use an Event 051 folder under the proper engine category, for example:

- `gfx/event_pictures/051_heat_wave/`
- `gfx/interface/decisions/051_heat_wave/`
- `gfx/interface/ideas/051_heat_wave/`
- `gfx/super_events/051_heat_wave/`

Exact paths and sprite files require live repository inspection.

Temporary evidence belongs under `docs/assets/051_heat_wave/` during implementation and should be removed only after durable provenance and runtime crosswalks are promoted into permanent documentation.

# Event and report images

## HW-ART-01 Global onset

**Use:** Entry event.

**Scene:** A large city and rail district under oppressive midday heat. Civilians seek shade, water is being distributed, railway workers inspect track, and haze softens the distance.

**Source mode:** Generated documentary art unless a suitable archival composite is selected.

**Avoid:** Modern skyline, modern bottled-water branding, cinematic orange grading, burning city, weather map as main subject.

## HW-ART-02 Water queue

**Use:** Urban water report.

**Scene:** Period civilians waiting with metal and glass containers at a municipal pump or tanker. Guards or officials manage distribution without making violence the main subject.

**Source mode:** Generated documentary or sourced archival.

## HW-ART-03 Exhausted troops

**Use:** Military heat report.

**Scene:** Period infantry resting under improvised shade beside a road or desert position, with canteens, medics, and supply vehicles visible.

**Source mode:** Sourced archival when a defensible World War II image exists. Generated documentary otherwise, without depicting a named real person.

## HW-ART-04 Railway deformation

**Use:** Rail restriction or damage report.

**Scene:** Track workers inspecting heat-stressed rails under direct sun, with a slow train or maintenance equipment in the background.

**Source mode:** Generated period documentary because modern rail safety photographs may not fit the era.

## HW-ART-05 Night factory shift

**Use:** Night-shift decision or report.

**Scene:** Factory workers arriving or working at night under period lighting, open windows, fans, water barrels, and crowded transport.

**Source mode:** Generated documentary.

## HW-ART-06 Harvest failure

**Use:** Agricultural crisis report.

**Scene:** Farmers examining damaged grain, dry irrigation channels, and stressed livestock. The image should show specific material loss.

**Source mode:** Generated documentary or period archival.

## HW-ART-07 Drying landscape

**Use:** Evolution II warning.

**Scene:** A familiar agricultural or forested landscape visibly losing vegetation and water, with settlement and infrastructure still present.

**Source mode:** Generated documentary.

## HW-ART-08 Recovery

**Use:** Recovery report.

**Scene:** Water service, rail, or agriculture returning after the heat. Visible damage remains, so the image does not imply complete restoration.

**Source mode:** Generated documentary.

## HW-ART-09 Scorched World

**Use:** Evolution III super-event.

**Scene:** A broad human landscape under a pale, overwhelming sun. A major road or city edge is nearly empty in daylight, water is guarded, distant smoke or dust obscures the horizon, and moving columns leave toward cooler ground.

**Source mode:** Generated documentary or restrained period illustration.

**Avoid:** Planet viewed from space, fantasy fire raining from the sky, modern climate graphic, mushroom cloud, text, or a simple desert panorama without human consequence.

# Decision category picture

## HW-CAT-01 Heat Wave response

**Use:** Main decision category picture.

**Reference:** Inspect the canonical vanilla decision-category picture shelf and its contact sheet before generation.

**Composition:** A compact horizontal or reference-matching panel showing water distribution, rail or industrial heat, and a distant city under haze. Keep one strong focal subject.

**Source mode:** Generated full-canvas art.

**Static sprite:** Proposed `GFX_051_heat_wave_category_picture`.

**Animated sprite:** Proposed `GFX_051_heat_wave_category_picture_animated`.

Exact dimensions must match the inspected consumer. The reference family currently uses a 114 by 101 canvas, but that is not a universal runtime guarantee.

# Category animation

## Purpose

The animation communicates current intensity through real source frames. It should not be a decorative loop that plays identically at every stage.

## Frame plan

Suggested 8 frames at a slow 3 to 5 frames per second.

| Frame | State | Visual change |
| --- | --- | --- |
| 000 | low heat | light haze, active daytime movement |
| 001 | rising | stronger shimmer and fewer pedestrians |
| 002 | severe | water distribution becomes prominent |
| 003 | extreme | rail or factory work slows, air appears denser |
| 004 | peak | pale sky, guarded water, minimal daytime movement |
| 005 | easing | haze begins to weaken, work crews return |
| 006 | recovery | water and maintenance activity resumes |
| 007 | loop bridge | visually close to frame 000 only when the category uses an ambient loop |

A state-driven implementation may use separate static frames or short loops per band instead of one full-cycle loop when that better matches the verified category consumer.

## Animation rules

- Every meaningful frame must be separately generated or edited from the approved seed according to the frame plan.
- Do not create the motion by shifting, scaling, recoloring, blurring, or changing opacity on one still.
- Build a horizontal frame sheet and a static fallback.
- Preserve the intended opaque full-canvas treatment for the category picture.
- Provide source frames, processed frames, sheet PNG, sheet DDS, static PNG, static DDS, preview GIF, contact sheet, manifest, and GFX handoff.
- The preview GIF is review-only.

# Decision icons

Each icon needs separate source art designed for its final surface.

| Asset ID | Working subject | Proposed sprite role |
| --- | --- | --- |
| HW-ICON-01 | Water ration card and canteen | Emergency Water Rationing |
| HW-ICON-02 | Public hall with water and shade | Cooling Centres |
| HW-ICON-03 | Soldier, canteen, and shaded rest marker | Army Heat Protocols |
| HW-ICON-04 | Grain sheaf with irrigation channel | Harvest Protection |
| HW-ICON-05 | Rail, thermometer, and maintenance tool | Railway Heat Maintenance |
| HW-ICON-06 | Factory window and moon | Night Shifts |
| HW-ICON-07 | Closed factory gate and heat symbol | Controlled Shutdown |
| HW-ICON-08 | Crate, grain sack, and ship or train | Emergency Food Imports |
| HW-ICON-09 | Pump, reservoir gate, and wrench | Pumping Protection |
| HW-ICON-10 | Train and civilian column | Organized Heat Evacuation |
| HW-ICON-11 | Water pipe and repair tool | Restore Water Service |
| HW-ICON-12 | Rail and rebuilding crew | Repair Critical Corridor |

Decision icons should remain readable at the inspected native decision size. They must not be resized focus icons.

# State and idea icons

## HW-STATE-01 Local Heat Stress

A small state-condition family with distinct severity frames or sprites. It should use a clear sun and heat-distortion motif without relying only on color.

## HW-STATE-02 Water Service Failure

A dry pump or broken main motif.

## HW-STATE-03 Environmental Degradation

Cracked soil with a declining plant or water line. Separate from Local Heat Stress.

## HW-IDEA-01 National Heat Emergency

Used only if the implementation requires a country idea for the active national priority or category state. Prefer one staged idea with route-specific tooltip behavior instead of several stacked ideas.

# News and world milestone images

Dedicated news images are justified for:

- first global onset, if the framework uses news presentation
- first permanent desertification
- first large cross-border heat displacement
- Evolution III super-event buildup

Do not create a separate image for every report.

# Achievement icons

Create one separate achievement icon triplet for every implemented achievement. The base icon should depict the actual challenge, not reuse decision or idea art.

Final files belong directly in `gfx/achievements/` and must match full achievement IDs. Each achievement needs base, grey, and not-eligible states according to the established workflow.

# Provenance and manifests

For every sourced or generated asset, record:

- stable asset ID
- source mode
- prompt or source URL
- creator, archive, date, and rights where sourced
- source checksum
- processed checksum
- target dimensions
- runtime path
- proposed sprite
- review status
- alpha or opaque-background treatment
- final consumer
- blocker or uncertainty

# Asset review gates

- matching vanilla or Chaos Redux reference inspected
- period technology and clothing fit
- no modern props
- no generated text
- no white matte or fake transparency on icons
- no source-frame drift in animation
- event art remains readable at in-game size
- separate art for separate icon types
- final DDS exists in runtime folder
- sprite handoff names every consumer
- no runtime reference points into `docs/assets/`

