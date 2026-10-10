# Event 085 — Super-Event Research and Production Prompt

Create the four Ten Plagues super-events defined in [Part 17](085_ten_plagues_of_egypt_spec_part_17_super_event_directions.md), which holds the triggers, picture, text and audio directions and the research gates.
Read Parts 8, 9, 16 and 17 and the narrative source notes, then follow the repository rules and the `chaos-redux-super-events`, `chaos-redux-event-assets` and `chaos-redux-subagents` skills.

## Research

- Spawn `chaosx_super_event_text_researcher` with a self-contained prompt giving the four slots, their triggers, the worldwide adaptation, religious neutrality, the picture directions and the handoff path.
Use primary texts for the Exodus passages and authoritative sources for any other quotation; return what Part 17 lists for each slot.
- Spawn `chaosx_super_event_audio_researcher` with an equally complete prompt; each slot needs a distinct real recording with composition and recording rights, acquisition route, passage and cut points.
- Firstborn means people of all ages, no named real victim is established, and the escape text never claims that damage, famine, disease, grief or war has ended.

## Production

The four 457 × 328 pictures come through the [asset prompt](085_ten_plagues_of_egypt_asset_prompt.md).
The parent obtains and processes the licensed audio under `sound/085_ten_plagues_of_egypt/`, allocates collision-free super-event IDs, and wires localisation, picture, sound, volume, queue behavior, presentation settings and once-per-episode guards.
Playback never controls the plague clock.

## Deliverables

Research and production evidence under the event's super-event and asset documentation folders, candidate text with sources, audio provenance and cuts, picture handoffs, the runtime ID mapping and unresolved rights issues.
Rejected candidates stay labeled as rejected.
Unresearched wording or unresolved audio remains blocked.
