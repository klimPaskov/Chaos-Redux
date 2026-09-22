# Super-event research prompt: Event 074

Research and complete the single planned super-event for Event 074 from `docs/specs/074_japan_lands_in_usa_specs/`.
Read design Parts 1, 5 and 7, the source register, and the current `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-subagents` and `AGENTS.md` instructions.
Working output belongs under `docs/plans/074_japan_lands_in_usa_plans/`, with source and asset evidence in the event asset workspace.

## Exact narrative and trigger context

Japan and the United States are already at war.
The event has established a major Japanese army on the Pacific mainland without requiring Japanese naval supremacy or victory elsewhere.
The super-event is reserved for the first realized tier III operation with at least 90 percent of its authorized immediate force actually issued, at least three working Pacific ports and access in at least two Pacific mainland states.
It is a one-time presentation for the episode.
A selected tier III flag, a single-region fallback or unissued reserve armies are insufficient.
The gameplay grant must not be withheld merely because this presentation gate remains unmet.

The text should convey the scale of a continental front, the failure of previous assumptions about distance, and the practical American mobilization response.
It must work with the actual government and leader setup.
Do not require a historical president, a particular emperor, a historical date or a claim that Japan won the Pacific naval war.
The fictional invasion must not be presented as a real photographed historical event.

## Research responsibilities

Spawn `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` with `fork_turns="none"` where the tool exists.
Pass the spec root, this prompt, the exact gate above, current world-text constraints, relevant sources, output paths and the question independently to each role.
The text researcher owns final title direction, sourced quotation candidates and context, cultural-reference checks, final button wording and approved localisation handoff.
The audio researcher owns relevant recordings, original source, exact excerpt, duration, composition and recording rights, attribution and usable local delivery.
The parent reconciles the final coherent package and the visual scene with the asset worker.

Unresearched titles, button text, quotes, cultural remarks, slogans, lyric fragments, allusions and audio choices are blockers.
Do not turn the working evolution name, asset filename, a candidate quote or an achievement label into final super-event text without the required review.
Do not fabricate a quotation or attribute a line about this fictional invasion to a historical speaker.
Any short quotation must preserve its source meaning and comply with applicable quotation limits.

Use a sourced 60–120-second audio excerpt and do not exceed 120 seconds without explicit approval.
Check both the composition and the particular recording.
A public-domain composition does not establish that a modern recording is reusable.
Do not silently use generated audio, a default game cue or a different generic music file when a requested source cannot be cleared.
Present unresolved rights or access as concrete blockers.

## Visual and technical handoff

Coordinate one 457 × 328 period-style fictional invasion scene through the event asset workflow.
Avoid embedding final quote or title text into the picture.
The normal super-event interface supplies localisation.
The source plan contains no finished image, audio, title, quote or allocated slot.

Read the existing super-event registry and allocate a noncolliding slot only after the audit.
Do not guess an unused number.
Follow the existing `GetSuperEventImage` and text getter consumers and the shared super-event queue.
Wire audio through `global.current_super_event_audio_id` and `play_current_super_event_sound = yes` as required by the current skill and registry.
Use the validated naming family `chaosx_super_event_<slot>_sound_<suffix>`.
Planned local audio belongs under `sound/074_japan_lands_in_usa/super_event_<slot>_<name>.wav`, with registrations in `sound/chaosx_sound.asset` and the required `music/chaosx_music_track_list.html` entry.
These are handoff patterns, not evidence that files or a slot already exist.

Deliver the final reviewed text package, exact sources and quotation context, cleared audio with start/end timestamps and duration, rights notes, attribution, image consumer, allocated slot, registry changes, and one-time trigger tests.
Report any missing component explicitly.
Do not mark the super-event complete until the actual final files and runtime consumers satisfy the package.
