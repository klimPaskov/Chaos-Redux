# Event 097 Collaboration: Super-Event Research Prompt

Use `chaos-redux-super-events` for the complete Competing Orders super-event package. Spawn `chaosx_super_event_text_researcher` for the quote and button remark and `chaosx_super_event_audio_researcher` for the track, each with a self-contained prompt built from this file. Route the image to `chaos-redux-event-assets` through `chaosx_generated_event_art` using the direction in `097_collaboration_asset_prompt.md`.

Read first:

- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_3_occupation_capitulation_and_governments.md`, section Competing orders
- `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_6_ai_presentation_achievements.md`, section Super-event: Competing Orders

## The moment

At least two different powers each rule two or more defeated countries through governments installed by Event 097. Rival systems of prepared regimes, built from the networks that exist in every country, now govern part of the world. The super-event fires once per campaign when this first becomes true.

Role: irreversible political shift. It is not a reveal, a defeat, or a world end.

## Slot

Super-event slot 97 belongs to an Event 015 super-event. Use the next free slot confirmed against `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` at implementation time, and add rows to all five selectors: image, title, quote, remark, and description.

## What the player should feel

Cold recognition that the world has been reorganized by people who were ready to serve whoever arrived, with no great catastrophe needed. The player should look at their own ministries differently afterward.

## Title direction

Short. About governments or loyalties changing hands, or about orders built from prepared regimes. It must avoid generic apocalypse wording, avoid triumph, and avoid the word warning.

Status: research required. The title is not final until the super-event workflow records it.

## Description direction

Explain that several powers now rule defeated countries through their own former officials, that these systems compete, and that no government can be certain who in its own service already answers to another capital. Keep uncertainty about who organized the first networks. Do not list effects or mechanics. Do not name real collaborators.

The implementation agent writes the final description from this direction.

## Main quote direction

A traceable, preferably public-domain quote about loyalty, betrayal, serving foreign masters, or the ease with which officials change their allegiance. Candidate source families: classical political writing, scripture, historical speeches, period political essays, or literature in the public domain. The quote must be short enough for the super-event frame, verified word for word, and attributed with a source link and confidence level. A quote attributed to Emilio Mola about the fifth column is acceptable only if the exact wording and source can be verified. Otherwise it must be rejected.

Status: research required.

## Button remark direction

A short, grim, or ironic remark from the viewpoint of an official who has served several governments, or a period phrase about serving whoever is in charge. Modern copyrighted lines must stay very short. The remark must be sourced and documented.

Status: research required.

## Audio direction

A structured, restrained musical recording with a formal or ceremonial character, such as a slow march, a choral piece, or a chamber work. It should sound like an official ceremony that nobody in the room believes in. Length between one and two minutes after editing, public domain or clearly licensed for both composition and recording. No drones, stingers, ambience beds, or generated tones.

The track must be unique to this super-event. It is placed under `sound/097_collaboration/` with its own audio id, base sound definition, and settings-volume wrappers, and it is listed in `music/chaosx_music_track_list.html` with full source and rights details.

Status: research required.

## Image direction

See the asset prompt. Generated, period-documentary, a formal installation ceremony in a provincial government hall with an unnamed foreign army at the edge of the frame, no readable text, no real persons.

## Research note

Record every candidate and the final package in `docs/super_events/097_collaboration_super_event_research.md` with all fields required by the super-event skill.

## Blockers

Unresearched titles, button text, quotes, cultural remarks, slogans, allusions, and audio choices are blockers. The implementation agent must not turn these directions, the working label Competing Orders, an achievement name, or an asset name into final super-event localisation.
