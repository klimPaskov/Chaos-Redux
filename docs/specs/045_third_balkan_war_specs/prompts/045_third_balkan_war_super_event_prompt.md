# Super-event research and production prompt for Event 045

Use `chaos-redux-super-events`, `chaos-redux-event-assets`, and the narrow super-event text, audio, and image subagents. Read the full Event 045 specification and research notes before selecting any final wording, quote, image, or music.

Event 045 has two justified super-event roles.

## Super-event A: outbreak

### Trigger meaning

The event has successfully created a valid multi-country Balkan war and recorded its opening camps. The war is already active when the presentation appears.

### Text direction

- Title direction: short identification of the Third Balkan War or the return of the Balkan powder-keg problem
- Description direction: several regional armies are already moving, the dispute is known, and outside powers are deciding whether to contain or exploit it
- Button direction: restrained dark humour about historical recurrence, diplomatic optimism, borders, or the belief that a regional war can stay regional
- Quote direction: verified public-domain or historical wording about Balkan rivalry, alliance failure, mediation, territorial ambition, or the danger of a regional crisis
- Tone: ironic at the recurrence, serious about the fighting
- Avoid: jokes about deaths, ethnic stereotypes, generic world-in-flames language, invented quotes, and final text copied from the planning spec

The frequently attributed Bismarck remark about a foolish event in the Balkans is not approved. Use it only if the text researcher finds reliable original or scholarly provenance. Otherwise reject it and document the rejection.

The 1925 Petrich incident may support a brief researched allusion, but the stray-dog origin story has competing accounts and must not be stated as certain fact.

### Image direction

Use the outbreak image brief in `prompts/045_third_balkan_war_asset_prompt.md`. The image should show mobilization and frontier movement rather than a map.

### Audio direction

Find a unique, intentional musical recording with a verified license. Search first for period-appropriate public-domain or clearly licensed Balkan, southeastern European, military, orchestral, or folk material whose recording rights are also usable. Avoid choosing one belligerent's triumphal national recording as the neutral event cue unless the context and rights clearly justify it.

The final cue should normally be one to two minutes after editing. Preserve the source, verify composition and recording rights separately, convert to game-ready WAV, register a unique audio ID, create the settings-volume wrappers, use `play_current_super_event_sound = yes`, and update the canonical music catalogue.

## Super-event B: Another World War

### Trigger meaning

Balkan War Escalation has reached at least `85`, opposing major powers or major-led factions are directly fighting, and one wider-war proof in the specification is met. Event 045 records the Balkan conflict as the origin crisis and hands control to normal war and faction systems.

### Text direction

- Title direction: the regional war has become a wider world war
- Description direction: direct major-power conflict and fronts outside the original theater are now visible facts
- Button direction: grave, brief, and free of triumphant humour
- Quote direction: verified historical or public-domain wording about alliance escalation, war spreading beyond control, or the cost of failed restraint
- Tone: serious and final about scale, while not describing a terminal world end
- Avoid: apocalyptic extinction language, invented prophecy, and lines that imply the campaign has ended

### Image and audio direction

Use a visually distinct world-war handoff image. Select a unique licensed musical cue with wider scale and no reuse from another super-event unless the user explicitly approves the exact reuse.

## Required research output

For each super-event provide:

- stable role and proposed slot
- at least three title directions before final selection
- at least three quote candidates with exact source, author, work, year, link, public-domain or copyright status, and confidence
- at least three short cultural remark directions where the role permits one
- rejected candidates and reasons
- selected final title, description, button, and quote only after source checks
- image source mode and asset handoff
- at least three audio candidates with title, creator or composer, performer or recording source, source URL, license, duration, usage terms, attribution, and suitability
- selected source download and processed WAV
- base sound definition and settings-wrapper IDs
- final audio ID and helper wiring plan
- permanent research note under `docs/super_events/`
- update to `music/chaosx_music_track_list.html`

Any unverified quote, cultural reference, or recording remains blocked. Do not fill a missing slot with default art, default audio, or provisional text and call it complete.
