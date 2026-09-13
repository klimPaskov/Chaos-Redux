# Event 059 asset production prompt

Use `chaos-redux-event-assets` as the owning skill. Read `AGENTS.md`, the complete Event 059 spec pack, the event-assets skill, the generated-art and icon-artist subagent contracts, and the current report-event and achievement reference catalogs before creating assets.

Produce the complete visual package for Event 059. Do not edit gameplay, localisation, AI, event, cluster, or achievement logic.

## Asset 1: Event report image

### Role

A single report image for the activation of The Offensive. The same image may be reused by evolution reports because all stages represent the development of one global military doctrine.

### Source mode

Generated fictional documentary scene through `chaosx_generated_event_art` with `fork_context=false`.

### Visual direction

Create a nationality-neutral late-1930s or 1940s combined-arms offensive. Show period tanks and infantry moving through a breached defensive line, with artillery smoke, forward transport, and a small number of period aircraft establishing depth. The scene should communicate concentration, movement, and prepared follow-up. It should resemble a wartime press photograph after project processing.

### Avoid

- readable text
- national flags or identifiable political insignia
- modern weapons, optics, electronics, armour, vehicles, aircraft, road furniture, or buildings
- graphic gore
- a map-only composition
- a conference room or diplomatic meeting
- cinematic science-fiction lighting
- excessive empty sky or foreground
- a composition that becomes unreadable at report-event size

### Consumer and output

Inspect the current report-event reference family and processor before locking paths or dimensions. The planning target is 210 by 176 pixels with the established black-and-white and sepia-card treatment.

Use the stable basename `chaosx_event_059_the_offensive` unless repository inspection finds a conflicting established convention.

Deliver:

- untouched full-resolution generated source PNG
- exact generation prompt and generation record
- source review at full resolution
- processed native-size PNG preview
- final DDS in the correct event-scoped runtime folder
- proposed sprite name and verified GFX handoff
- manifest with dimensions, format, alpha mode, source mode, checksums, processor settings, consumer, and status
- native-size contact or comparison view when useful

## Asset 2: Achievement icon family

### Role

Artwork for the planned Event 059 achievement defined in `059_the_offensive_achievement_prompt.md`.

### Source mode

Original generated icon art through `chaosx_icon_artist` with `fork_context=false`.

### Visual direction

Show a small fortified shield or compact defensive line breaking and turning back a large offensive arrow. The weaker defensive symbol must remain visually dominant enough to read as successful resistance. A restrained period map texture can support the motif. Do not include letters or numbers.

### Consumer and output

Inspect the current Chaos Redux and installed vanilla achievement definitions, texture sizes, state order, alpha treatment, and native reference family before generation. The planning size is 64 by 64 for the completed state.

Create every state required by the current consumer, including completed, grey, and not-eligible variants when the standard triplet is in use. Generate source artwork for the icon itself. Mechanical greyscale or state processing is allowed only where the inspected workflow permits it.

Deliver:

- source PNG
- native-size completed PNG
- every required state PNG and DDS
- stable sprite names and verified GFX handoff
- transparent-edge and native-size review
- manifest with state order, dimensions, alpha, source mode, checksums, consumer, and status

## Quality gate

Reject any asset with broken period identity, unreadable native-size composition, fake text, unresolved crop, wrong consumer dimensions, missing state, bad alpha, or unverified path. Do not use placeholders, resized unrelated art, primitive geometry, or another event's icon.
