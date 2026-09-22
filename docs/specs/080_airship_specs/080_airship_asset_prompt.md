# Event 080: Asset-production prompt

Produce the complete Airship visual package through `chaos-redux-event-assets`, with `chaos-redux-scripted-gui` and `chaos-redux-frame-animation` where relevant. Read all seven spec parts, especially Part 7, and the source report before production. No final artwork or original route DDS files were produced or inspected by the planning session.

## Inspect actual references first

Use the canonical project reference library under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`. The supplied skill records the user's installation root as `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`. Resolve the current real repository location instead of assuming this Windows path exists in another environment.

Inspect the matching contact sheets and individual native-size examples for report images, news, super-events, decision icons, ideas, and achievements. Recover and visually inspect the actual Airship route maps and marker assets before proposing changes. If a required reference contact sheet is missing, build and label it from the real reference images and update the reference README and catalog according to the skill. Do not claim to have inspected an image based only on its filename.

The authoritative route must remain unchanged. No historical Graf Zeppelin route, replacement world map, invented city stop, or randomly positioned airship marker may replace it. The route crosswalk is not a complete geographic binding. Coordinate with the route owner before drawing final overlays.

## Required visual inventory

Use neutral production IDs and record exact final runtime paths in a manifest. Final localisation is separate.

Create larger ship-panel art and native-size marker art for baseline, Grand Tour, experimental-equipped Grand Tour, and Flying City. Each needs sound, damaged, and critical-condition variants, for twelve presentation combinations in each relevant consumer size. Include a grounded intact/impounded state, a grounded write-off, and distinct wreck treatment where needed. The Flying City must remain readable through a few large structural features, not tiny detail.

Create the native route layers needed to distinguish completed route, upcoming route, original stops, actual location, delay, a genuine diversion branch, missing contact, and the actual crash location. Preserve existing valid trail imagery and finalise the index-121 state. Do not bake dynamic values or clickable controls into a background.

Provide country report scenes for departure, flyover, service, passenger interior, reception, inspection, technical work, medical transfer, damaged approach, radio search, forced landing, impoundment, rescue, grounded write-off, homecoming, ordinary crash, Flying City crash, and ocean loss. Compatible ordinary scenes can be reused across several related stories. Major outcomes must remain visually distinct.

Provide news scenes for departure, major landmark arrival, diplomatic impoundment, serious emergency, confirmed disappearance, major crash, and successful homecoming. Provide the rare Flying City catastrophe scene in coordination with the super-event specialists. Do not portray the impact as a nuclear strike or add landmarks that are not present at the actual site.

Create a coherent decision icon family covering standing orders, repair, specialist inspection, supplies, passenger transfer, local reception, search, rescue, technical trial, refit, departure, and abort. Create the needed aviation-prestige and mourning idea art without exceeding the spec's active spirit budget. These symbolic families must match their own canonical references, not borrow focus frames.

Create all eight achievement subjects listed in Part 6 and the achievement prompt, including their complete three-state runtime outputs. No country flags, leader portraits, focus-tree art, or runtime 3D meshes are planned.

## Correct format and processing

Country reports use the 210 by 176 slanted monochrome or sepia card with the prescribed transparent-corner processing. Use the actual `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` workflow. News images use 397 by 153 monochrome output. Super-event art uses 457 by 328. Decision icons are 32 by 32 and idea icons 64 by 64. The original map and its ship panels use their inspected native consumer dimensions, which were not verified by the planning session.

For achievements, inspect `icons/achievements/contact_sheet.png` and the actual template folder. Preserve `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png` byte-for-byte, at their exact 64 by 64 alignment. Verify their full SHA-256 values from the current skill before use.

Generate one genuinely transparent colour subject per new achievement through image generation, without an achievement frame, text, square background, fake transparency checkerboard, or red cross. Derive the grey and not-eligible source layers deterministically according to the skill. Use `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` with the complete three-state input. Validate exact decoded compositing against the immutable backgrounds and overlay.

All three achievement DDS files go directly under `gfx/achievements/`, named from the exact registered achievement ID with base, `_grey`, and `_not_eligible` suffixes. Do not create `gfx/achievements/080_airship/`. Keep the shared registry's single-root structure and update its owner-approved sections, localisation, GFX, and manifest consistently.

For other runtime assets, use the appropriate existing event-owned `080_airship` folders. DDS conversion must satisfy the skill's strict legacy 32-bit BGRA, header, alpha, mip, and decoded round-trip requirements for each consumer. Inspect decoded runtime pixels, not only the source PNG. Retain source art, processed files, provenance, and conversion evidence.

## Animation, GUI, and review

Normal two-day marker changes are progression states, not a fabricated animation. If approved, author genuine propeller or exhaust frames for underway states and actual smoke or flame frames for an emergency. Use the frame-animation pipeline with a complete manifest, supported atlas dimensions, timings, static fallbacks, and native testing. A pulsing flat whole image is not an adequate substitute.

Create and review reference images for the event-owned map layout before native GUI work. Record the image-to-element mapping and agreed state coverage. The UI worker must inspect the actual hierarchy and render matched scenarios, including departure, a stop, repair, diversion, missing contact, each form, a crash, and success at supported resolutions. Review hit regions, long labels, large values, and contrast on real game backgrounds.

There is no extra decorative category picture beside the interactive map. Do not redesign shared event log, event details, settings, or super-event framework surfaces. Native UI values and actions must remain separate from decorative art.

## Provenance and delivery

Fictional high-chaos scenes and symbolic icons normally use image generation. Historical source material can guide grounded appearance or supply licensed appropriate ordinary scenes. Verify rights for every source image. Never claim a historic image documents the fictional Flying City. Route named real-person portrait work to the portrait specialist only if a later accepted design actually introduces that requirement.

Provide a manifest with production ID, consumer, actual dimensions, source mode, provenance or prompt, source and processed files, runtime path, sprite binding, SHA-256, conversion result, native-size review, and approval or blocked status. Use temporary event working records under `docs/assets/080_airship/` only while work is incomplete. Final runtime references must not point into documentation folders.

Perform a hash-aware final source-to-runtime synchronisation so old mapped files cannot overwrite the reviewed candidate. Supply contact sheets and full matched visual evidence. Do not claim production complete while a required form, report, route state, achievement triplet, or runtime binding is missing or unreviewed.
