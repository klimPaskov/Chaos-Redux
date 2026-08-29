# Asteroid Incoming, Part 9: Visual and Audio Direction

## Visual identity

Event 028 should feel grounded in period observation, civil defense, and physical destruction. The presentation can use fictional documentary images because the event itself is alternate history. Generated art should match 1936 to 1945 photographic technology, clothing, architecture, vehicles, observatory equipment, and news composition.

The visual package should avoid modern space-agency rooms, modern emergency vehicles, satellite imagery, cinematic science-fiction control panels, glowing holograms, readable generated text, and modern disaster-film grading.

## Map presentation

### Main impact

Use the existing thermonuclear-scale explosion visual for the main center. The effect should be visually larger than fragment effects and should occur at the locked state.

The visual is presentation only. The asset and script names should avoid suggesting that the gameplay source is nuclear where practical.

### Fragments

Use the normal nuclear-scale explosion visual for each fragment center. Resolve the visuals in a short sequence after the main effect so the player can understand that several sites were struck.

The sequence should not hold the game for a long montage. The global report and map state carry the lasting information.

### Crater states

The main crater and fragment sites need clear state-modifier icons and map tooltips. Existing wasteland visual treatment can be reused only when it can show a nonradioactive asteroid source.

The main crater should be visually distinct from ordinary damaged states. Fragment sites should be distinct from the main crater and from radioactive fallout.

## Required event images

### Main entry report image

- Surface: report event
- Canvas: 210x176
- Source mode: generated fictional documentary image
- Direction: period observatory interior or outdoor telescope team tracking a bright object, with scientists studying plates, calculations, or instruments
- Mood: controlled urgency and limited time
- Avoid: modern computers, space suits, control-room screens, readable equations, and a visible impact scene before the choice

### Target emergency report image

- Surface: report event
- Canvas: 210x176
- Source mode: generated fictional documentary image
- Direction: civil-defense transport, field hospitals, railway evacuation, or government archives being moved under a strange bright sky
- Mood: practical emergency preparation
- Avoid: gore, modern ambulances, generic war-room maps, and a mushroom cloud

### Affected-country impact report image

- Surface: report event
- Canvas: 210x176
- Source mode: generated fictional documentary image
- Direction: collapsed rail lines, dust-covered streets, damaged industrial outskirts, rescue crews, and civilians moving through debris
- Mood: regional destruction and organized response
- Avoid: identifiable real tragedy photography, modern rescue gear, and nuclear symbols

The same base report image can serve several affected countries when dynamic text supplies local identity. The image should be designed as an event-wide disaster visual, not a fake picture of one named real city.

### Fragment report image

- Surface: report or global fragment news support
- Canvas: 210x176 when used as report art
- Source mode: generated fictional documentary image
- Direction: a smaller distant impact, debris trail, and regional damage under period photographic limits
- Avoid: copying or resizing the main impact super-event image

### Close-passage news image

- Surface: news event
- Canvas: 397x153, black and white
- Source mode: generated fictional documentary image
- Direction: observatory dome, telescope silhouette, crowded public viewing point, or bright object crossing a night sky
- Mood: relief and scientific unease
- Avoid: modern astrophotography, color nebula imagery, and a visible collision

### Main impact super-event image

- Surface: super-event
- Canvas: 457x328
- Source mode: generated fictional documentary image
- Direction: a vast impact flash and rising debris over a period landscape or industrial region, seen from a distant survivable viewpoint with clear scale
- Mood: physical catastrophe, not fantasy magic
- Composition: one dominant light and debris column, readable horizon, period buildings or transport for scale, room for the super-event text crop
- Avoid: mushroom-cloud imitation as the sole subject, modern skyline, space view, Earth-from-orbit view, text, flags, and a map

The image should remain usable for any dynamic target country. It must not contain country-specific flags or landmarks.

### Decision category picture

- Surface: Event 028 recovery category
- Reference family: canonical decision-category picture references
- Source mode: generated fictional documentary image
- Runtime size: inspect the active consumer before production, using 114x101 only as the reference-family canvas
- Direction: rescue rail line, dust masks and filters, damaged infrastructure, and a darkened sky in one coherent scene
- Purpose: identify the recovery category and current disaster theme
- Avoid: fake buttons, fake meters, dynamic numbers, maps with colored states, and text

## Required icon families

Every icon family needs separate source art suited to its own size.

### State-modifier icons

Create distinct icons for:

- Main asteroid crater
- Catastrophic impact zone
- Major impact zone
- Outer shock zone
- Fragment crater
- Heavy fragment damage
- Light fragment damage

Use the verified state-modifier consumer and reference family for final canvas and framing. The family should share a visual language of fractured ground, debris, darkened sky, broken rail, and crater material.

### National idea or dynamic-modifier icons

Create 64x64 spirit-style icons for:

- Global dust stage
- National dust protection
- National impact-recovery burden
- Main crater material control
- Fragment material control

Dust and mineral icons must be visually distinct. Dust should use atmosphere, filters, or obscured industry. Minerals should use dense metallic or crystalline fragments without fantasy glow.

### Decision icons

Create separate 32x32 icons for:

- Mobile hospitals
- Emergency rail corridor
- Debris clearing
- Water and filter distribution
- Supply-spine reconstruction
- Outer-ring industry restoration
- Worker rehousing
- Factory dust hardening
- Transport and reserve protection
- Atmospheric observation network
- Crater perimeter security
- Material survey
- Access-route fortification
- Rival-site reconnaissance

Each icon should use one simple subject and strong silhouette. Do not derive them by resizing idea or achievement art.

### Achievement icons

Create one 64x64 completed, grey, and not-eligible triplet for each accepted achievement. The achievement prompt defines themes and tracking.

## Asset progression

Dust presentation should change through modifiers and text. A large animated asset package is not needed. Static stage icons or controlled idea variants are enough to show Residual Haze, Global Dust Veil, Impact Winter, and Severe Impact Winter.

If the implementation later proves that an animated category picture adds clear state information, it requires a separate frame-animation plan with real source frames and a static fallback. Static art is the accepted baseline.

## Audio role

The impact super-event needs one unique final musical cue.

The cue should:

- Be a real licensed or public-domain musical recording
- Fit a scientific disaster and global impact
- Use period, orchestral, choral, solemn, or restrained modern-classical character where licensing allows
- Run about one to two minutes after editing
- Have a clear source, creator or composer, performer or recording source, license, and attribution record
- Use the shared settings-aware super-event sound path

The cue should not be a drone, test tone, noise bed, explosion sound, oscillator layer, trailer cue with unclear rights, or reused track from another super-event without explicit approval.

Map explosions can use the established impact presentation audio already tied to the visual effect when appropriate. The super-event music remains separate.

## Text and quote research

The visual package does not choose final title, quote, button remark, or audio. The super-event research worker should verify several candidates and return a sourced recommendation. The final image, text, quote, and track must describe the same campaign moment.

## Asset package requirements

The asset production handoff should retain source images, prompts, processed PNG previews, final DDS files, contact sheets, transparency checks, dimensions, source mode, and sprite proposals. Final runtime files must live in the event-scoped gameplay folders. Temporary evidence can remain under the Event 028 asset workspace until the implementation and review are complete.
