# Super-event research prompt for Event 016 Brilliant Scientist

Research exactly six mapped packages. International recognition and qualifying defeat are conditional at runtime but still require complete text, image, unique audio, source, licence, localisation, documentation, and wiring handoffs.

Use visible super-event reservations 88 through 93 in this order: recognition, formation, global threat, Laboratory World, Strategic Singularity, qualifying defeat. Do not use Event 020 slots 85 through 87. Laboratory World and Strategic Singularity use world-end scenario IDs 11 and 12.

Use `chaosx_super_event_text_researcher`, `chaosx_super_event_audio_researcher`, and the appropriate image subagent. Spawn each with `fork_context=false` and pass only the narrow brief it needs.

## Source design

Read:

- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_8_super_events_world_end_and_aftermath.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_9_assets_animation_and_localisation.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md` for image work

## Packages to research

1. International recognition, conditional reveal.
2. Kruger State formation, with peaceful, violent, or takeover description direction.
3. Global Kruger threat.
4. Laboratory World terminal order.
5. Strategic Singularity and Fallout terminal event.
6. Defeat aftermath, conditional on a long global crisis.

Do not omit or merge any package. The parent rejected removal of international recognition. Runtime conditions determine whether recognition or defeat appears in a campaign; they do not reduce the production inventory.

## Text research

For every retained package, find and document:

- Several real main quote candidates.
- Exact wording.
- Author or speaker.
- Work, speech, scripture, document, or archive.
- Year or approximate period.
- Reliable source URL.
- Attribution confidence.
- Copyright or public-domain note.
- Fit to the exact super-event role.
- Several short button-remark or cultural-reference candidates.
- Whether each remark is a direct quote, title reference, short fragment, or paraphrase.
- Modern copyright risk.
- Selected main quote, selected remark, and backup options.

Do not invent quotations. Do not use quote-site copy without verification. Keep modern copyrighted fragments very short. Prefer public-domain scientific, philosophical, political, literary, religious, or historical sources for the main quote.

Final titles also require deliberate research and selection. Avoid generic apocalypse titles. Working role labels in the spec are not final localisation.

## Audio research

For every retained package, select a unique real musical track unless the user explicitly approves a named reuse.

Required documentation:

- Title.
- Composer or creator.
- Performer or recording source.
- Source URL.
- Composition rights.
- Recording rights.
- License and usage terms.
- Confidence.
- Duration.
- Attribution text.
- Original source path.
- Final OGG path.
- Suggested audio ID and sound wrapper.
- Editing, trim, fade, volume, and conversion notes.
- Why the track fits the role and pacing.

Final OGG must be 44.1 kHz. Prefer one to two minutes or document the exception. Do not use generated test tones, oscillators, drones, ambience beds, beeps, one-shot stingers, commercial film or game music, or tracks with unclear rights.

## Image direction

Use `chaosx_generated_event_art` because Kruger and all super-event scenes are fictional alternate history.

Target size is 457x328. Use strong central composition, period-authentic visual technology, and no generated text.

- Recognition: Kruger with scientists, guards, instruments, and international observers.
- State formation: dominant project route visible through clone, robot, bestiary, portal, temporal, alien, or human-science state identity.
- Global threat: organized project army or captured scientific center.
- Laboratory World: ordered global laboratory society, route-aware.
- Singularity: human-scale laboratory city or core overtaken by the terminal phenomenon.
- Defeat: soldiers, scientists, survivors, or inspectors entering a captured laboratory.

## Research note

Create or update `docs/super_events/016_brilliant_scientist_super_event_research.md` with all candidates, selections, sources, licenses, image directions, final paths, IDs, blockers, and implementation notes.

Do not edit localisation, events, GFX, GUI, sound definitions, or spreadsheets. The main agent owns final wiring.
