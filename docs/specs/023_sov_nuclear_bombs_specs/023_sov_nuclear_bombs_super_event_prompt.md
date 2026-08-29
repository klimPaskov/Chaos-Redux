# Event 023 super-event research and implementation prompt

Create the complete nonterminal super-event package for the first confirmed nuclear exchange among major powers caused or observed through Event 23.

## Role

The super-event marks the transition from testing, monopoly, threats, or limited use into a real exchange involving at least two nuclear majors.

It fires once when a confirmed major-to-major nuclear detonation occurs during an active exchange crisis.

It does not fire for:

- A test.
- A threat.
- A failed launch.
- A strike on a nonmajor.
- A storage accident.
- A single major striking a nonnuclear minor.

It is nonterminal. It must not set `world_end`, replace Fallout, reuse the Fallout image or audio, or claim the manual Final Silence scenario.

## Required reading

Read:

- `AGENTS.md`.
- `chaos-redux-super-events`.
- `chaos-redux-event-assets`.
- `chaos-redux-events`.
- `chaos-redux-subagents`.
- Event 23 Parts 5, 7, and 8.
- Current super-event registry, scripted localisation, sound definitions, audio catalog, and event trigger source.

## Research routing

Spawn with `fork_context=false`:

- `chaosx_super_event_text_researcher` for verified quote candidates, button remark or plain reaction, exact attribution, source confidence, and copyright notes.
- `chaosx_super_event_audio_researcher` for a unique licensed or public-domain musical recording, legitimate download, conversion, and audio handoff.
- `chaosx_generated_event_art` for the image after the parent locks its dimensions, basename, and sprite.

The parent owns final localisation, `.gfx`, sound definitions, slot, trigger, docs, and catalog alignment.

## Text direction

Title:

- Short and specific to a confirmed nuclear exchange.
- Avoid generic apocalypse titles.
- Do not reveal Fallout unless the shared terminal route has actually begun.

Description:

- Mention confirmed detonations, shortened response time, failing communications, evacuation, and retaliatory preparation.
- Keep the focus on observed global consequences.
- Do not list mechanics or hidden AI conditions.

Button:

- Use a short researched cultural remark only when it fits and remains within copyright limits.
- A plain severe reaction is acceptable.
- Avoid generic `We must act` wording.

Quote:

- Must be real, verified, and traceable.
- Prefer public-domain literature, scripture, historical political writing, philosophy, or period text about war, destruction, judgment, responsibility, or failed control.
- Do not invent or misattribute a quote.

## Image direction

Generate one period-authentic documentary-style scene showing a confirmed exchange among major powers.

Include a dominant nuclear flash or distant detonation, damaged or crowded communications, evacuation or military warning activity, and 1936 to 1945 visual details.

Avoid modern command screens, modern missiles without a verified campaign route, satellite views, abstract diagrams, title cards, readable generated text, gore, celebratory framing, and visual reuse from Fallout.

## Audio direction

Select a unique structured musical recording.

Preferred tone:

- Severe orchestral.
- Choral or liturgical.
- Period modernist.
- Funeral or lament character.

Rules:

- Prefer one to two minutes after editing.
- Verify composition and recording rights separately.
- Preserve original source and license evidence.
- Pure drones, alarms, sound-effect beds, test tones, generated audio, oscillators, and placeholder music are forbidden.
- Do not reuse another super-event track without explicit user approval.

Final path pattern:

`sound/023_sov_nuclear_bombs/super_event_<verified_id>_<verified_name>.wav`

## Wiring

- Verify an unused or correctly reusable super-event slot.
- Lock title, description, button, quote, image, and audio to that slot.
- Set a unique Event 23 exchange audio ID.
- Use `play_current_super_event_sound = yes`.
- Add the base sound and all settings-volume wrappers.
- Update `GetSuperEventImage` and every relevant scripted-localisation selector.
- Trigger once from the confirmed multi-major exchange threshold.
- Preserve the shared Fallout presentation for the terminal route.

## Documentation

Create or update:

`docs/super_events/023_sov_nuclear_bombs_super_event_research.md`

Record:

- Role and trigger.
- Final title and text keys.
- Quote, author, work, source, confidence, and rights note.
- Button remark source when applicable.
- Image source mode, final path, sprite, and asset provenance.
- Track title, composer, performer or recording source, URL, license, duration, original path, final WAV, sound ID, wrappers, and conversion.
- Super-event slot.
- Confirmation that the package is nonterminal and distinct from Fallout and Final Silence.

Update `music/chaosx_music_track_list.html` with the final track and super-event ID.

## Acceptance

- Real multi-major exchange threshold.
- Fires once.
- Correct image, text, quote, button, and audio.
- Unique licensed track.
- Settings-aware volume.
- No clipping, raw keys, or mismatched slot content.
- No `world_end` flag.
- Fallout remains separate.
- Final asset and audio files exist.
- Research and rights are complete.
- No placeholder remains.
